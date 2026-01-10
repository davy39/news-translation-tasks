---
title: 'How to manage colors in your images and videos: latest trends and best practices'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T18:15:07.000Z'
originalURL: https://freecodecamp.org/news/color-management-for-the-web-the-challenges-from-iphone-to-chrome-b07cb44ad21b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UQygvO5FoRqMZuzlPO_4yg.jpeg
tags:
- name: Design
  slug: design
- name: Photography
  slug: photography
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anton Garcia Diaz

  During the last world football cup, few people knew that only the flags of Argentina
  and France out of the top 10 teams could be accurately displayed on a standard HDTV.
  All the remaining flags colors were clearly out of gamut. T...'
---

By Anton Garcia Diaz

During the last world football cup, few people knew that only the flags of Argentina and France out of the top 10 teams could be accurately displayed on a standard HDTV. All the remaining flags colors were clearly [out of gamut](https://dot-color.com/2018/06/14/2018-world-cup-watching-in-4k-hdr-makes-a-difference/). That is, standard displays were not capable of reproducing the colors properly. Only those fans using wide gamut sets could see their colors in a 4K HDR broadcast.

As for a web workflow, it is much more involved than the display properties. Textures, saturation, hue or brightness may be far more important in other industries than in football — just think of fashion or the art imagery in ecommerce. In such cases, clean color management is key to deploying healthy and reliable image and video processing and optimization pipelines.

However, color management in ecommerce and in general in web workflows may unfold as a tricky issue. My recent experience with complex ecommerce teams involving photographers, retouchers and devops to debug and deploy [image and video optimization](https://abraia.me) solutions only reinforces this idea.

In this article, I shortly revise the basic concepts involved in color management, the best practices, and the challenges posed by the latest trends in display technology.

### Color in the human eye

Humans with healthy color vision have three types of color detectors in the retina. Each of these types of detectors respond with different strengths to spectral colors, from red to violet. As a result, any physical color that we perceive can be represented as the combination of three chromatic primaries.

This fact allowed us — nearly 90 years ago — to define the first [colorimetry](https://medium.com/hipster-color-science/a-beginners-guide-to-colorimetry-401f1830b65a) standard to convert the physical magnitudes of light into a numeric representation uniquely related to colors. It set the basis to accurately represent any color (of light reaching the eye) by a simple array of three numbers.

### Cameras and displays

Digital cameras and displays were designed to convey images of scenes that a human eye is able to see as if it were right there looking at them. So, cameras capture a trichromatic representation of the scene and code it in a digital file.

To do this, cameras _simply_ :) have three types of light detectors (R, G, and B) like our retina has. Likewise, displays transform digital values in trichromatic signals that drive the generation of light to recreate the image stored in a digital file. To do it, displays _simply_ :) have three types of light emitters (R, G and B).

It seems easy: The camera mimics the eye and the display projects light to mimic the scene, finally conveying it to the eye, anytime, anywhere.

But there are…

### Some fundamental problems

Some related to the physics and some related to perception.

#### Need to calibrate

Just to start with, the spectral sensitivities of the three detectors of a camera sensor are different — very different indeed — from our eye’s light detectors (our eye’s detectors are not R, G, and B). Moreover, different camera sensors exhibit quite different behaviors (their R, G, and B are different). Color perception is clearly non-linear with physical magnitudes like the intensity of light. But sensors are typically linear with light intensity.

In the end, this means that to provide accurate color representations, cameras should be calibrated. Calibration is done by shooting an image of a pattern of colors. A color profile is then created that transforms the sensor response into a standard representation of color. But this should be done for different lighting.

Put in simple words, if we seek true color fidelity we would need to calibrate to correct color for each new scene! And any slight change of lighting means that the scene has changed as well. Fortunately, depending on the specific need of accuracy and the flexibility of the workflow, [the requirements of calibration can be relaxed](https://www.dpreview.com/articles/6497352654/get-more-accurate-color-with-camera-calibration-).

Something similar happens to displays, but the other way. They translate the colors coded within image files into light emitted. Slight changes in the amount of light emitted have an impact on the color effectively displayed.

That’s why professional displays need to be calibrated from time to time. The light emitted for some primaries is checked and a display color profile is created. This profile is used to transform the stored pixel values to actual light with the intended color. Needless to say, user displays are not calibrated, but they usually have a factory color profile instead.

We should acknowledge that current LED technology has greatly limited the variation of color properties among different units of the same display model and also in the same display through time.

#### Still… perception tricks

If all this were not enough, our brain excels in assuring color constancy under different lighting conditions. To do it, a variety of mechanisms are constantly adjusting perception in order to match the expected color based on the scene context. This is done regardless true values of the physical color. You may pick the digital RGB values in A and B in this classic illusion (check the [original here](https://upload.wikimedia.org/wikipedia/commons/b/be/Checker_shadow_illusion.svg), since Medium alters the image).

![Image](https://cdn-media-1.freecodecamp.org/images/XO28ZzoXDgz4FUWSHEBWssaOUkvX8GyGqbeO)
_[color constancy](http://illusionoftheyear.com/cat/top-10-finalists/2018/" rel="noopener" target="_blank" title="">Our brain tricks our perception</a> to ensure <a href="https://en.wikipedia.org/wiki/Color_constancy" rel="noopener" target="_blank" title=") under variable lighting conditions_

They are exactly the same: The display sends the same light from each of them. Even after knowing so, you will see A darker than B. I see it as I’m writing this. Such a tricky perception is a powerful reason for many photographers to adjust colors by hand rather than using a calibrated scene reference.

### Color management

However, things may still get worse, much worse. At this point, we should have noticed that speaking about color with the same language is important if we want to keep consistent. To accomplish this need, we should manage color. In other words, our software should be color managed. A failure to manage color in a web workflow will undermine the consistency of the user experience.

With this aim, different color spaces have been developed. Each color space aims to support a use case in the best possible way. Three examples of use cases are:

* average display technology
* printing of photos
* 4K HDR video and cinema

Each color space has an associated color profile to interpret the stored RGB values in a file. There are many handy tools out there to check the color space of an image. For instance, the inspector tool of Preview in Mac.

![Image](https://cdn-media-1.freecodecamp.org/images/WnGZ7G3v-sUnTyioaxdeNRrOvAIVlZgL7taJ)

![Image](https://cdn-media-1.freecodecamp.org/images/JroDDhekpFIYRUbaredfEjut6AGSFsz24TC4)

![Image](https://cdn-media-1.freecodecamp.org/images/uh48YMtViR-W8UyPEFWC9GNsM8M8PYBewim4)
_Three examples of color profiles shown in Preview: one with an undefined color profile, other with the color profile of an iMac display, and one more with an sRGB color profile_

To check every detail about an image, I find it very convenient to use _exiftool._ It reveals the color profile, among many other metadata.

```
exiftool test.jpg
```

You should see something like this

![Image](https://cdn-media-1.freecodecamp.org/images/3jYcqsOx82Z31YuOaoa10s68L7kKUwYYBnqI)
_Fragment of exif data of an image coded in the sRGB color space_

With videos, Mediainfo is a handy tool with a simple and usable graphic interface. Putting the pointer over the _Video_ area, detailed metadata of the video appears, including the color space at the bottom.

![Image](https://cdn-media-1.freecodecamp.org/images/2YEAbslcKDEP4MmjjGrPSxKsuvwjFDt9s9hX)
_Capture of Mediainfo window with information on color profile highlighted in red_

#### Classic Color profiles

**sRGB: based on Rec. 709**

Created by HP and Microsoft, this color space was specially aimed at the Internet. It is based on BT.709 (or Rec 709) standard for video, adding gamma suited to CRT displays. But it’s also suited to average human perception. This means that it makes an efficient use of the dynamic range.

This is the color space [universally supported](https://www.w3.org/Graphics/Color/sRGB.html) throughout the web. Any image (or web element) without an explicit color profile (that is an undefined color space) will be interpreted by any web browser as being sRGB. Moreover, any decent display is sRGB capable: it can reproduce the whole sRGB color gamut. At the time of this writing, this is the safest color space in a web context.

If you assure that ALL your workflow, from studio to web delivery, is (well) done in sRGB, then the colors of the images in your web will be consistent for everybody. You may be confident of this.

In case you find a non sRGB image and you need a quick fix, [Little CMS](http://www.littlecms.com/) is a handy tool to get the job done. Whatever color profile has the image, you may convert it to sRGB by simply using

```
jpegicc -q100 input.jpg output.jpg
```

However, remember that the best practice is working from the beginning in sRGB. When transforming from a wider space, out of gamut colors may be treated differently — and in some cases colors may be clipped while in other cases they may be washed out. It depends on the [rendering intent](http://www.johnpaulcaponigro.com/blog/6088/rendering-intents-compared/).

The inconvenience of sRGB is that your gamut will be more limited than a good percentage of current display technology, with this percentage increasing steadily. Recall the beginning of this article. Unless you are French or Argentinian, chances are that you won’t see your country colors properly in a standard sRGB monitor. Or in other contexts, everybody buying cloths online is deciding purchases based on untrue colors (shown on uncalibrated displays!). But if the web sticks to sRGB, the mismatch experienced by each user will be at least consistent, limiting the chance of bad surprises.

**Adobe RGB**

It is the classic color space used in the graphics industry. It has a wider gamut than sRGB and covers fairly the gamut relevant in the production of prints. To work with it, you will need a profesional calibrated wide gamut display capable of Adobe RGB.

Unless images are intended to be printed rather than viewed in a display, this color profile does not make sense in a web workflow. I include it here because I have found it several times in such a context.

Since it is the preferred color space of photographers and retouchers that print their work, some people think of it as implying higher quality than sRGB. Adjusting color in a color space and saving the image in a different one may end up being a waste of time and bringing unexpected results, specially in the presence of highly saturated tones.

If you are asked to optimise pristine images with this color profile you are likely facing upstream issues coming from the retouching or studio teams. Problems may be even worse if you find Adobe ProPhoto, with an even larger gamut.

#### New wide gamut color spaces

**DCI-P3 (or simply P3).**

This color space has been adopted by Apple in their wide gamut displays since 2016. Other brands recently embracing wide gamut have [also adopted P3](https://gizmodo.com/why-every-smartphone-screen-looks-different-1820748943). Although with a similar size to Adobe RGB, it spans a different gamut, better suited to displays — light projection technology — instead of prints. It is an intermediate step towards UHDTV, aimed at 8k TV and film industry. It is good for high quality streaming that may cater to 4K HDR capable displays.

The use of P3 results in much richer and deeper colors, with a true impact on user experience and color fidelity. Back to the world cup example, P3 would greatly improve the color fidelity and deliver true colors for most fans. It’s easy to think about a similar benefit for imagery in a fashion, cooking or traveling websites.

**UHDTV /Rec. 2020**

This color space has been designed for 4k and 8k HDR TVs. It brings a wider gamut compared to P3. It contains P3 as well. Even for HDR TVs this standard is [still the future](https://www.rtings.com/tv/tests/picture-quality/color-volume-hdr-dci-p3-and-rec-2020). It does not make much sense in a today’s web workflow.

#### **Comparing gamuts**

If you own a wide gamut display and enjoy healthy color vision, a first hand visual check is the best and quickest way to understand and assess the differences among color profiles. A good starting point is to use wide gamut images specially prepared to [compare color spaces](https://webkit.org/blog-files/color-gamut/comparison.html).

### Good practices with color

Unless you are determined to be a wide gamut pioneer, color management will be synonym of enforcing the sRGB color space throughout the image processing pipeline.

A good practice is to calibrate the camera at least with a [dual illuminant calibration](http://blog.xritephoto.com/2010/05/x-rite-colorchecker-passport-dual-illuminant-profiles-part-1/). Of course, the use of specific calibrations for specific lighting will always be better. In the studio, the more fixed your lighting settings are (so you don’t need to recalibrate), the better. If you directly shoot jpegs in sRGB instead of RAW, your calibration should be done in sRGB.

When iPhones are used to shoot, the color space may be an issue since [iPhone cameras are set to DCI-P3 by default](https://photo.stackexchange.com/questions/98792/which-color-space-is-used-by-my-iphone-8-photos).

Just after shooting, any color correction in darkroom software should be already done in sRGB. Retouching should be done in sRGB. You will avoid issues related to rendering intent choice. The same applies to artwork and visual creativities.

The software used should be color managed. This is the case of most image editing and graphics packages. In the case of video, there was a notable exception: Adobe Premiere Pro versions prior to October 2018 [did not manage color](https://premierepro.net/color-management-premiere-pro/).

If Premiere is used in post-production for web, the best practice is using a calibrated sRGB display. Otherwise, you may end up with video colors that will change (typically washed out) when viewed in the web. This is why so many Premiere users on iMAC displays usually oversaturate their videos, in order to avoid washed out exported results.

If the sRGB rule is observed, the only risks to color due to generation and optimization of derivatives will be [compression artifacts](https://abraia.me/docs/image-optimization/#jpeg-compression) related to low q values or excessive chroma downsampling.

Don’t be fooled by old stuff posted saying that browsers are not color managed. It’s only the proof that being highly ranked in Google search is no guarantee of accurate and up to date information. All the major web browsers (from Safari, to Firefox, Edge, or Chrome) are currently color managed and capable of interpreting ICC profiles.

If you have many iOS and macOS users you may be tempted by the P3 color space. You would bring them a much more realistic experience, with far more vibrant colors.

But in 2019 it is still a risky move. All the other users with average sRGB displays may experience either washed out or oversaturated images. The impact will always depend on the specific picture and the browser, since browsers may use different [rendering intents](http://www.johnpaulcaponigro.com/blog/6088/rendering-intents-compared/). For instance in macOS — as of January 2019 — Chrome (version 71) and Safari (version 12) use perceptual intent, while Firefox (version 64) uses colorimetric intent.

Serving two manually adjusted versions to take the wide gamut advantage on iOS users while still serving optimum sRGB images… would require you to adjust colors in both spaces. The benefits are unlikely to balance the burden for photography and retouch teams.

### Summary

A good practice from studio to web is sticking end to end to the same color space. In most (practically all) cases this means sticking to sRGB.

When different sources of images and video cater to the workflow, this requires awareness for all the people involved in the image creation and processing chain.

However, display technology has recently moved from racing on resolution to racing on color gamut. So, we should keep an eye on the P3 color space and the tech used by our users. As more and more of them purchase wide gamut displays, switching to images with a P3 color profile may start to make sense.

