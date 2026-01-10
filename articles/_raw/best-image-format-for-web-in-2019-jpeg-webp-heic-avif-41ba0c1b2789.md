---
title: 'The Best Image Format for the Web: JPEG, WEBP, HEIC, or AVIF?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T15:08:57.000Z'
originalURL: https://freecodecamp.org/news/best-image-format-for-web-in-2019-jpeg-webp-heic-avif-41ba0c1b2789
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z3SfTvHOfvZiz1mr7uOODA.jpeg
tags:
- name: Design
  slug: design
- name: image
  slug: image
- name: performance
  slug: performance
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anton Garcia Diaz

  After decades of the unrivaled dominance of JPEG, recent years have witnessed the
  appearance of new formats — WebP and HEIC — that challenge this position.

  These have only partial, but significant, support by major players among ...'
---

By Anton Garcia Diaz

After decades of the unrivaled dominance of JPEG, recent years have witnessed the appearance of new formats — WebP and HEIC — that challenge this position.

These have only partial, but significant, support by major players among web browsers and mobile operating systems. 

Another new image format — AVIF — is expected to enter the scene in 2019 with promise of sweeping through the whole web.

In this article, we’ll start with a short revision of the classic formats, followed by a description of WebP and HEIC/HEIF. We’ll then move on to to explore AVIF, and end with a summary putting all the main points together.

Comments on advantages and drawbacks build both on the review of available authoritative reports and first-hand observations during the development and deployment of [tools for image optimization pipelines in ecommerce workflows](https://abraia.me/).

### Classic image formats for the web with universal support

Let’s remind ourselves, in chronological order, of the three most important classic formats for web images.

#### **GIF**

GIF supports LZW lossless compression and multiple frames that allow us to produce simple animations.

The major limitation of this format is that it is constrained to 256 colours. This was reasonable back when it was created in the late 80’s, since the same limitation applied to existing displays. However, with the improvement of display technology it became apparent that it was not suitable to reproduce any smooth color gradients, like those found in photographic images. We can easily spot the color banding that it produces.

However, GIF allows lightweight animation with universal support. This feature has kept the format alive until today in use cases not sensitive to quality issues, the most typical being small animated images with few or no colors.

#### **JPEG**

The king of the image formats for web was developed to support digital photography workflows.

With a usual 24 bit depth, it provides far more color resolution (not to be confused with range or gamut) than the human eye can discern. It supports lossy compression by exploiting known mechanisms of human vision.

Our eyes are more sensitive to medium scales than to fine details. Consequently, JPEG allows us to discard fine details (high spatial frequencies), by an amount controlled by a quality factor. Less quality means less detail is preserved. Besides, we are much more sensitive to details with high luminance contrast than details with only chromatic contrast.

So, JPEG internally recodifies RGB (Red, Green, and Blue) images in one luminance and two chroma channels. This allows us to use chroma subsampling to discard more detail only in the chroma channels. It’s worth noting that JPEG codifies images in blocks of 8x8 pixels.

As we reduce the quality factor and/or apply more aggressive chroma subsampling, we start to get increasing artifacts of ringing, halos, blocking, or blur. An issue with JPEG is that depending on the image content, artifacts may appear at different quality factor values. The wildest difference appears when comparing the effects on natural photography with the effects on artwork. Since artwork (shapes, fonts) usually rely on sharp edges, they start to produce artifacts even for small amounts of detail discarded.

For photos, JPEG easily delivers a reduction of file weight by a factor of 10 with barely noticeable artifacts, compared to lossless compression.

#### **PNG**

This lossless graphics format was developed to replace GIF, addressing its color banding (and licensing) issues. It was needed for images with a considerable amount of artwork, for which JPEG produced large artifacts even with minimal compression rates.

It supports transparency and an improved compression compared to GIF. Since it does not discard information, PNG does not produce artifacts. Of course, this is at the expense of heavier image weight in the presence of many different color gradients, compared to lossy compression.

It succeeds in exploiting a frequent characteristic of artwork: Unlike photography — that features a continuum of colours with subtle variations — artwork pictures usually feature few well-defined colours.

So, PNG compresses images by mapping large amounts of pixels to a simple discrete palette and saving a lot of bits as a result. Compared to GIF, it delivers much higher quality with usually far fewer bytes.

### Newcomers with partial support: WEBP and HEIC based on HEVC

Mechanisms used by video codecs to compress streams may be classified into two main types: inter-frame and intra-frame. While the first one exploits the redundancies along time, intra-frame mechanisms focus on reducing redundancy inside a given frame, without any dependency on the rest. This compression mechanism may be applied to still images.

The explosion of video sharing — with mobile networks at its heart — and the steady increase of display resolution has driven the efforts on new coding standards to achieve the highest possible efficiency in compression.

So, new image formats are emerging as derivatives of the new video coding standards. These new image formats offer larger feature sets than JPEG and promise relevant savings in file weight with improved visual quality.

#### **WEBP**

Google developed this format with the aim to provide a single web-capable image format to deal with all the typical use cases.

Importantly, it seeks to achieve lighter images than JPEG, without penalties on visual quality. It uses more complex operations — like block prediction — and is a derivative of the VP8 video codec. It supports lossless compression and unlike JPEG, it allows transparency and animations that may combine images coded with both lossless and lossy compression.

In principle, it should serve as a replacement for JPEG, PNG, and GIF. An important drawback has been the lack of universal support. Until recently, WebP had been restricted to Google-backed software like the Chrome browser and Android-native applications.

However, with the [announcement](https://www.zdnet.com/article/firefox-and-edge-add-support-for-googles-webp-image-format/) that Edge and Firefox (excluding iOS Firefox) are to introduce WebP support in 2019, it’s evidently gaining traction. It’s also worth noting that Apple — Safari and iOS — does not support WebP yet.

#### **HEIC/HEIF**

This format brings a significant evolution in two different regards.

Firstly, the [file container supports the largest feature set among image formats](http://nokiatech.github.io/heif/technical.html) available. It supports, for instance, multi-frame images with multi-frame compression — a key feature for efficient HDR, multi-focus, or multi-view images.

Secondly, it supports many types of non-image data with a remarkable flexibility. Currently, most images using this container are compressed with a derivative for images from the H265/HEVC video codec, developed to efficiently cope with the 4k and 8k resolutions featured by the latest generation displays. HEVC coding involves more complex operations with fewer restrictions than JPEG. It achieves a much higher compression efficiency at the cost of slightly higher coding times — not a problem at all in web workflows.

Like H265, HEIC based on HEVC is backed by Apple. It has native support in iOS and macOS, but — mostly due to patent and licensing issues — it is not supported by the rest of platforms (Android, Windows). Even in macOS, Safari doesn't support it. iOS apps appear to be the only viable usecase for HEIC in the web. 

So a big question arises: should we offer WEBP/HEIC alternatives and JPEG, with PNG versions as a fallback?

Let’s look at each case...

### Should I serve WEBP derivatives?

Google claims that this format produces much lighter images than JPEG with comparable quality. However, independent tests have pointed that this result [is not consistent across different measures of quality](https://research.mozilla.org/2013/10/17/studying-lossy-image-compression-efficiency/), and weight reduction is, in most cases, balanced by increasing blurriness.

In our own tests with ecommerce images, we saw file savings for WebP, but at the price of more blur and less detail. Although, we also saw less risk of ringing and blocking artifacts, which we’d consider more visually annoying than blur.

As WebP lacks support by Apple browsers and operative systems, we _do not_ generally recommend serving WebP derivatives competing with JPEG. Such moves would increase media management complexity with limited benefits.

This situation would change if Apple started supporting WebP.

If this were the case, then the extended feature set of WebP and the lighter images produced may be worth its use, effectively simplifying image management workflows.

To try WebP yourself, a classic tool like [ImageMagick](https://www.imagemagick.org/script/index.php) is a good option. It makes easy-to-compare image versions with different settings of quality and resolution for both WebP and JPEG. Results can be viewed with Chrome.

```
# Convert to WEBP quality 60
convert input.jpg -quality 60 output_60.webp
# Convert to JPEG quality 60
convert input.jpg -quality 60 output_60.jpg
# Convert to WEBP quality 60 and width 450px
convert input.jpg -resize 450 -quality 60 output_450_60.webp
```

Different combinations of quality and resolution will have different effects in each case, as the compression algorithms work differently. So, check your relevant file sizes on several images to get a grasp of the potential savings and the best settings for a given use case.

### Should I serve HEIC derivatives?

The advantage of HEIC (over JPEG) is clear. Weight reduction is consistently significant — about 50% — without loss of visual quality. The feature set supported is simply amazing.

The problem again is browser and operative system support.

Given the patent issues of HEVC and the hefty royalties associated, we can expect support to remain restricted to those in the Apple world. Since JPEG is already efficient in compressing images, the 50% of something small might not be worth enough to add complexity to our image processing workflow.

Certain cases using large images, with a major interest in visual quality AND with a large percentage of Apple devices in their user base should consider serving this format.

Performing tests with HEIC is very easy with a Mac. Preview allows us to export an image to HEIC and JPEG with different quality values and different resolutions. You won’t need to run many tests to see the clear and systematic difference between them.

![Image](https://cdn-media-1.freecodecamp.org/images/XRTmUucDfTZm0iiTDvreSpEauY-ymS3dP1Bb)
_Export to HEIC in Preview_

If you want to try something more flexible that may be integrated in a web image processing workflow, [GPAC](https://gpac.wp.imt.fr/2017/06/09/gpac-support-for-heif/) is worth a look.

### **What about AVIF?**

AVIF is the last of our contenders.

Like WebP and HEIC based on HEVC, AVIF is a derivative of the latest efforts in video standards. It also uses HEIF containers and so supports a complete feature set, encompassing all the main formats available. It brings much higher efficiency in compression inherited from the use of AV1 intra-frame coding mechanisms. These advantages make this format compelling.

Another significant advantage comes from the [Alliance for Open Media](https://aomedia.org/), the large consortium behind its development as a fully open approach, with an open license, free of royalties. Big players like Google, Netflix, Adobe, Mozilla, Microsoft, Facebook and Amazon — major actors in the web graphics and video scene — are backing this new format and making a case for a fast and wide adoption, both in software and hardware. While the stream format was frozen in March 2018 [with a reference code available](https://aomedia.googlesource.com/aom/+/master/av1), the first devices with hardware support for AV1 are expected by the end of 2019.

At the time of writing this article, the open source implementation of AV1 available may be still considered experimental and not suitable for production.

### **Summary**

JPEG will remain the king format for general images for web in 2019, and PNG will remain as a default option for images with significant artwork.

The reason? Universal support.

Anything that opens an image will open JPEG or PNG in 2019, just like in previous years and decades! So no doubt that these universal formats will remain in place for some time yet.

The benefits of WebP remain controversial. A clear advantage of WebP is its ability to also replace PNG, potentially simplifying image processing workflows. However, without universal support this advantage vanishes. This may change only if Apple changes their mind and WebP finally gets universal adoption, then it could be used as a replacement for all JPEG, PNG and GIF images.  
   
In contrast, HEIC images based on HEVC do offer clear benefits, especially for large resolutions. If traffic of iOS users is relevant for a website with large heavy images, it may be worth considering serving HEIC alternatives for them, with potential UX improvements, especially for slow mobile connections. Besides speeding up, HEIC assures quality, almost free of the annoying blocking and ringing artifacts that plague aggressive JPEG policies.

Although AVIF is expected for 2019, support and adoption will take time. But for sure, it is an image format to keep under your radar for the near future.

Of course, the use of a cloud service -through an [image optimization API](https://abraia.me/docs/api/) or an [image optimization plugin](https://medium.com/abraia/best-image-optimization-plugins-for-wordpress-benchmarked-20508f9a0a57)- will always remain an easy and straightforward alternative for getting the job done.

