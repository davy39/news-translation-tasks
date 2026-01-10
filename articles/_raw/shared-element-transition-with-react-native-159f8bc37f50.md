---
title: Shared Element Transition with React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T14:45:29.000Z'
originalURL: https://freecodecamp.org/news/shared-element-transition-with-react-native-159f8bc37f50
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XjqvwLtPW_Gwu8dtlubs7Q.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Narendra N Shetty

  In this post I will be talking about how to achieve Shared Element Transition with
  React Native for both iOS and Android.

  I have posted the code on GitHub and you can take a look if you want to jump right
  into it.

  Intent

  Lets tak...'
---

By Narendra N Shetty

In this post I will be talking about how to achieve Shared Element Transition with React Native for both iOS and Android.

I have posted the code on [GitHub](https://github.com/narendrashetty/photo-gallery-RN) and you can take a look if you want to jump right into it.

### Intent

Lets take a look at what we’re going to build. Below is a photo grid example where we’ll add a shared element transition. This way, we can transition smoothly between a grid and the details page for a photo we select.

![Image](https://cdn-media-1.freecodecamp.org/images/ZFx3Y2ZbOyPA2C6sM-GcnUcBYAmGywCLVdcg)

This is a much smoother and a continuous experience.

### Approach

Before we build this, let me tell you how the system works under the hood. Since React Native doesn’t support true shared elements, when we say we are doing a shared element transition between two screens, we aren’t technically sharing any elements. Instead, each screen has its own individual element.

![Image](https://cdn-media-1.freecodecamp.org/images/bGX-qwWTtkSs5V5u8-02ldcXmz1rqZTS7I2k)

What I am doing is passing the information about the shared element — such as its position and size — between these two elements.

![Image](https://cdn-media-1.freecodecamp.org/images/kYlMlrL69TVmnl05mbdzD15rBoYCuzmBirYl)

When the details screen launches, its background is set to transparent, and it hides all of its elements. It then alters the attributes of the shared element to the one passed, then makes it visible. It then animates itself to its natural position. As the transition progresses, the window background and the rest of non-shared elements slowly fade in until they’re totally opaque.

So while the element is not technically shared, this clever trick of smoke and mirror makes it appear that they are.

So now that we understand how this process works, lets go step-by-step to understand how the mock element has been shared, and how we can control animations.

#### Step 1: Entry and Exit Animation

I have two screens here: Grid and Details. From the Grid screen, we can launch the Detail screen by clicking on one of the images in the grid. Then we can return to the grid screen by hitting the back button.

![Image](https://cdn-media-1.freecodecamp.org/images/Pl0Q1HzBuRyzczRY9nr0pdpM6oNvXyKkVa3P)

When we go from Grid screen to Detail screen we have an opportunity to run two sets of transition animations — the Exit transition for the Grid screen, and the and Entry transition for Detail screen.

![Image](https://cdn-media-1.freecodecamp.org/images/XcGZR2W0yZxivXxgvtqNDYwkWgdMvJgFOkpo)

Lets see how we implement this.

Without any transition, this is how the app looks. Clicking on the individual image takes you to a detail screen.

![Image](https://cdn-media-1.freecodecamp.org/images/MaVm33kp41KI5dqxVTXt9qqSL3tb0nLLmzDw)

Let’s add an exit transition to the first grid screen. Here we use a simple fade out transition using the `Animated` api, which interpolates the opacity attribute of the grid screen container from 1 to 0.

![Image](https://cdn-media-1.freecodecamp.org/images/Mp3343DgX5cx1FwUyIiPlmBvychD3jvsHSCV)

Now that we have done that, here’s how it looks:

![Image](https://cdn-media-1.freecodecamp.org/images/CQYSnNoG9QDBSWoSCSBBgUGnjxHq90SWXT1w)

Not too bad. We see that the grid is faded out as we move onto the details screen.

Let’s now add another transition to the content of the detail screen as it comes in. Let’s slide the text into the place from the bottom.

This is done by assigning an interpolated `Animated` value to the `translateY` property of the text container.

![Image](https://cdn-media-1.freecodecamp.org/images/kAniu9N72G8oW5JQ8t89Rv54fWDAX0Oha1pU)

And here’s how it looks:

![Image](https://cdn-media-1.freecodecamp.org/images/X0YkE34bdPvzpf-0NhO83UVqvmStSjdCLYbU)

Well the title and the description slides in very nicely, but the image appears abruptly. This is because our transition doesn’t target image specifically. We’ll fix this shortly.

#### Step 2: Transition layer for the shared element

We now add a transition layer which appears during the transition, and contains only the shared element.

This layer is triggered when the image in the grid is clicked. It receives information about the shared element, such as its position and size from both the Grid screen and Details screen.

![Image](https://cdn-media-1.freecodecamp.org/images/pcenEA9bbx0zTzDUENkZcqOMExDp-5kM5S7x)

#### Step 3: Animation in the transition layer

We have the information in the transition layer about the source and destination position of the shared element. We just need to animate them.

Let’s first set the element based on the source position and size, then animate it to the destination location. This can be done in two ways. Let’s take a look at both of them.

#### By interpolating on the width, height, top and left

This is a straightforward approach. If we want an element to change from one size to another, and from one position to another, we modify the width, height, top, and left style properties of the element.

![Image](https://cdn-media-1.freecodecamp.org/images/eOQgovymgQ41um3qq6l6beKw6WCGQvauibKR)

And here’s how it looks:

![Image](https://cdn-media-1.freecodecamp.org/images/q7yNP2uN-IAHdH9mayvgoObVAQtGZuZ8JkgE)

### **Performance Analysis**

When using Animated, we declare a graph of nodes that represent the animations that we want to perform, and then use a driver to update an Animated value using a predefined curve.

Here’s a breakdown of the steps for an animation and where it happens:

![Image](https://cdn-media-1.freecodecamp.org/images/dRi4Q2MoujdxMhx3lhc1xuOxT76QlfrYfwvw)
_[https://facebook.github.io/react-native/blog/2017/02/14/using-native-driver-for-animated.html](https://facebook.github.io/react-native/blog/2017/02/14/using-native-driver-for-animated.html" rel="noopener" target="_blank" title=")_

* JavaScript: The animation driver uses `requestAnimationFrame` to execute on every frame and update the value it drives using the new value it calculates based on the animation curve.
* JavaScript: Intermediate values are calculated and passed to a props node that is attached to a `View`.
* JavaScript: The `View` is updated using `setNativeProps`.
* JavaScript to Native bridge.
* Native: The `UIView` or `android.View` is updated.

As you can see, most of the work happens on the JavaScript thread. If it is blocked, the animation will skip frames. It also needs to go through the JavaScript to Native bridge on every frame to update native views.

This problem can be solved by using `useNativeDriver`. This moves all of these steps to native.

Since Animated produces a graph of animated nodes, it can be serialized and sent to native only once when the animation starts. This eliminates the need to callback into the JavaScript thread. The native code can take care of updating the views directly on the UI thread on every frame.

The main limitation is that we can only animate non-layout properties. Things like `transform` and `opacity` will work, but flexbox and position properties like the one used above won’t.

#### Interpolating on transform and using useNativeDriver

Let us now animate using transform. This will require a some math to calculate the scale, x and y position.

With this implementation, if we’re scaling from a smaller image to a larger one, the image will pixelate. So we will render the larger image, then scale it down to its start size, then animate it up to the natural size.

We can get the start scale value with a line of JavaScript like this:

```
openingScale = sourceDimension.width / destinationDimension.width;
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uu8Zc1iNN--BSiIfdCTqojt0luL8BHAR-egU)

You see that the scaled image and original image don’t look the same that is because the aspect ratio of source image and destination image are different, so to solve it we will render the image with source aspect ratio based on destination dimension.

```
const sourceAspectRatio = source.width / source.height;const destAspectRatio = destination.width / destination.height;
```

```
if (aspectRatio - destAspectRatio > 0) {  // Landscape image  const newWidth = aspectRatio * destination.height;  openingScale = source.width / newWidth;} else {  // Portrait image  const newHeight = destination.width / aspectRatio;  openingScale = source.height / newHeight;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/tBaj-bwjbgJF7fAMylwSI6UV8uYAb1N1iKWq)

Now that the scale is correct, we need to get the new position based on the destination image. This can be calculated by the destination position minus half of the difference between the old dimension and new dimension. Which would equate to:

```
if (aspectRatio - destAspectRatio > 0) {  // Landscape image  destination.pageX -= (newWidth - destinationWidth) / 2;} else {  // Portrait image  destination.pageY -= (newHeight - destinationHeight) / 2;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1yeIZSVuZHDO1iz1MEvCKNjuATAg4V6Rhg6F)

That’s perfect! We now have the right dimension, and position for the transitioning image.

Now we need to calculate the translation position from which to animate the image. We’ll scale the image from the center, so we need to apply our translate considering that we are just moving the center of the photo. So we’ll just do some relatively easy math, by taking the source position plus half of the source dimension. This would equate to this:

```
const translateInitX = source.pageX + source.width / 2;const translateInitY = source.pageY + source.height / 2;
```

```
const translateDestX = destination.pageX + destination.width / 2;const translateDestY = destination.pageY + destination.height / 2;
```

We can now calculate the translate position by the difference between the center of source image and destination image

```
const openingInitTranslateX = translateInitX - translateDestX;const openingInitTranslateY = translateInitY - translateDestY;
```

With this found start scale and translate values we can animate using the `Animated` api.

![Image](https://cdn-media-1.freecodecamp.org/images/hOkwzd1c6IZMipdXM8CIb-uweTyeyi5Ayfxr)

![Image](https://cdn-media-1.freecodecamp.org/images/fBxxGcefWRGBUWg79GrsjQ-skEesabpXAyqF)

That’s it. We now have transition working. We can now use `useNativeDriver` since we are now animating only non-layout properties.

#### Step 4: Hiding the source and destination image during transition

In the previous gif, we saw that during transition, the clicked image was still in the same position, and the destination image appeared before the transition was complete.

Lets hide the source and destination image during the transition, so that it looks like the clicked image is the one animating to the detail screen.

![Image](https://cdn-media-1.freecodecamp.org/images/WYts4q5v-eE1cKe0LdmknhyqSWRjlMSMl-lU)

![Image](https://cdn-media-1.freecodecamp.org/images/d274Oc2ajmFOkxqMYrZ5j8prjGX8wpDOkte4)

Let now see the output.

![Image](https://cdn-media-1.freecodecamp.org/images/MMgWH7b2mCuu3dHlRiVaYARZw3qxVNANjjQz)

#### Step 5: Handle the back button

During transitioning into the detail screen using `Animated.timing()` we change the `AnimatedValue` from 0 to 1. So when back button is clicked, we just have to change the `AnimatedValue` from 1 to o.

![Image](https://cdn-media-1.freecodecamp.org/images/Sv5VtAXjEHDtjBkMmesIIig4aBpyUvL0Db0r)

![Image](https://cdn-media-1.freecodecamp.org/images/n-zn4mWQDo3SblEHj9gfUQwk5pVq5rwwcrty)

That’s it. You can check the code on [Github](https://github.com/narendrashetty/photo-gallery-RN) and try out the demo on [Expo](https://expo.io/@narendrashetty/photo-gallery).

[**narendrashetty/photo-gallery-RN**](https://github.com/narendrashetty/photo-gallery-RN)  
[_Contribute to photo-gallery-RN development by creating an account on GitHub._github.com](https://github.com/narendrashetty/photo-gallery-RN)[**photo-gallery on Expo**](https://expo.io/@narendrashetty/photo-gallery)  
[_An empty new project_expo.io](https://expo.io/@narendrashetty/photo-gallery)

Also checkout [Eric Vicenti](https://www.freecodecamp.org/news/shared-element-transition-with-react-native-159f8bc37f50/undefined)’s [broadcast on shared element transition](https://www.twitch.tv/ericvicenti).

Thank you for taking time and reading this post. If you found this useful please clap and share it. You can connect with me on Twitter [@narendra_shetty](https://twitter.com/narendra_shetty).

