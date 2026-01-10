---
title: 'Haptics for mobile AR: how to enhance ARKit apps with a sense of “touch”'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T17:51:48.000Z'
originalURL: https://freecodecamp.org/news/haptics-for-mobile-ar-how-to-enhance-arkit-apps-with-a-sense-of-touch-151d9e9c9950
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t8zy_q2Ynm3QowFPo8w6MQ.png
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: unity
  slug: unity
- name: user experience
  slug: user-experience
seo_title: null
seo_desc: 'By Neil Mathew

  I’m really excited about the future of haptics for AR and VR. It feels like the
  missing link between my HTC Vive and jumping into the OASIS with Parzival and Art3mis.
  So it’s not surprising that haptics is perhaps the most hotly antici...'
---

By Neil Mathew

I’m really excited about the future of haptics for AR and VR. It feels like the missing link between my HTC Vive and [jumping into the OASIS with Parzival and Art3mis](https://en.wikipedia.org/wiki/Ready_Player_One_(film)). So it’s not surprising that haptics is perhaps the most hotly anticipated tech in the XR community right now. Several companies like Microsoft and HTC, as well as startups like [SenseGlove](https://www.senseglove.com/) and [HaptX](https://haptx.com/), have shown demos of increasingly promising iterations of haptic gloves that I’m itching to try out.

Unfortunately, like most AR developers today, our work at [**Placenote**](https://placenote.com) is focused almost entirely on mobile AR platforms like **ARKit** and **ARCore**. Naturally, this got us thinking, **“Could haptics do anything for mobile AR?**”

Haptics have been an awesome addition to touch screens, from simulating tactile button clicks to silent notifications. But, after some frantic googling we realized that there’s actually been no real discussion about haptics for **mobile AR apps** so far… CHALLENGE ACCEPTED ??

### **The challenge of mobile AR**

We decided to dig into why haptics hasn’t made it’s way into mobile AR and it wasn’t hard to see why. Mobile AR is by far the least immersive AR medium. The consensus in the community is that it’s just a stop gap to the ultimate AR platform — smart glasses.

But mindset isn’t the only barrier here. We found that the mobile form-factor presents some unique challenges to the AR experience designer:

* unlike headsets, the phone screen is the display as well as the controller
* it’s impossible to bring your hands into the experience since you’re holding the phone.
* we still rely on touch screen interactions that are ambiguous in dimensionality — 2D or 3D touch?

Nevertheless, the reality is that, for the next few years and perhaps more, mobile AR is here to stay. There are a billion mobile devices in consumer pockets right now and only about a handful of AR headsets on their heads. As a developer, distribution for your apps trumps most other factors. In fact, in applications like indoor navigation and gaming, mobile has already proven itself as a viable medium for deploying AR experiences.

This brings us to the topic of haptics for mobile AR. At first, it might seem like there’s no real hope for haptics to enhance mobile AR experiences, but recent studies have actually shown otherwise.

### **In haptics, less is more**

There’s been a myriad of methods conceived to achieve haptic feedback. In general they fall under two broad categories — **kinesthetic haptics** (force feedback) and **cutaneous haptics** (skin sensations).

Kinesthetic haptics has widely been considered to be the more realistic haptic technology. It involves physical actuators, either grounded or ungrounded. These push and pull our fingers and other appendages in response to interactions with virtual objects. Intuitively, realistic force-feedback should perform vastly better than plain old vibrations. But a study published in [Science Robotics this year titled “The Uncanny Valley of Haptics”](http://robotics.sciencemag.org/content/3/17/eaar7010) has challenged these assumptions.

The researchers found that increasing the realism of haptic sensation doesn’t necessarily increase the quality of the AR experience. It often has a negative impact due to the uncanny valley of realism in simulations. They found that cutaneous haptics, which is essentially a combination of light touches and vibrations, did a lot better in fooling the brain deeper into the illusion. Strange results, but they basically realized that we’ve underestimated how good our brain is at filling the gaps in our sensation of reality.

> The situations where our brain steps in to fill the gaps is what I find most interesting about our perception of the sensation of touch. — Justin Brad, CEO of Osso VR

### **Bringing haptics to mobile AR**

Given these findings, why not test what cutaneous haptics can do for mobile AR? After all, haptics on mobile is not just about vibrating ring tones anymore.

Micro-Electro-Mechanical Systems (MEMS) on mobile devices have gotten a lot more sophisticated and capable of some pretty nuanced behaviors. Since the iPhone 7, Apple has upgraded the old basic rumble vibrations to what they now call the **Taptic Engine.** This is a lot more subtle and consists of **seven different types of haptic feedback** with varying patterns and strengths.

The haptic feedback modes available are:

* Selection Change
* Impact Light
* Impact Medium
* Impact Heavy
* Notification Success
* Notification Warning
* Notification Failure

![Image](https://cdn-media-1.freecodecamp.org/images/EKykqXsyuWpCeEGMquFljyCCzN6ug26uPhCm)
_The new iOS Taptic Engine (iPhone 7 onwards) has 7 different kinds of Haptic Feedback_

To learn more about the iOS feedback generator, [check out this Apple documentation](https://developer.apple.com/documentation/uikit/uifeedbackgenerator). At the end of this article, I will share some code you can use to quickly add these feedback types to your ARKit apps.

We **decided to experiment** with a number of these haptic feedback modes in our AR apps and I’m really excited to say that the results were a pleasant surprise to our team.The following are some examples of haptic implementations in our mobile AR apps.

### **Usage examples of haptics in mobile AR**

In our experiments so far, we’ve found that haptic feedback for mobile AR works well in five distinct scenarios. Here’s a description of each.

#### 1. Magnetic pointers (i.e. snap to grid)

A pointer locked along a planar surface is a commonly used feature in many ARKit apps, especially in measurement tools like [Air Measure](http://armeasure.com/) and [Magic Plan](https://www.magic-plan.com/). Since your phone behaves as a controller in mobile AR, the standard UX in measurement apps involves dragging a pointer along a surface to draw lines or polygons to measure things in the real world. Of course, when it comes to line drawing, magnetic pointers that snap to the end points and edges of lines are seen everywhere — from PowerPoint to Photoshop.

We found that subtle haptic feedback indicating a “snap” in pointer position is a great enhancement. It almost feels like your phone, (i.e your controller) is physically moving to snap into place.

I was really happy to see that **Apple’s new app “Measure”** actually uses haptic feedback in their UX. It’s an amazingly subtle implementation and you can see a GIF of it in action below. An “Impact Medium” is fired when the pointer snaps to the edge of the plane.

![Image](https://cdn-media-1.freecodecamp.org/images/5h7tXFoybj35qprzl6G1EJIOrljyh-G6o2T-)
_Apple’s Measure App_

#### 2. Hit testing (feeling real world surfaces)

Another common feature in ARKit apps is the hit-test. This is implemented as a ray-cast from a point on the screen — either a touch point or the center — to a surface in the real word. It is generally used to add a 3D object at the point of contact. A slight haptic sensation can help the user understand that a surface was “hit”. We found two methods that work well here:

**Pinning**  
In this example, a marker is added to the scene at the hit point. An “Impact Light” helps users sense the “pinning” of the marker in 3D space. Of course, the downside to this is you can’t quite sense the “depth” of the hit point — in other words, how far the pin is from the user.

![Image](https://cdn-media-1.freecodecamp.org/images/5RQoGLCzDtV5l8bEtaqGmVs7ObuPGxdGGC98)

**Grazing**  
An alternative to pinning is the grazing method of hit testing. In this case, a constantly updating marker previews where a marker might be added to a scene. We found that a series of haptic impulses, based on the magnitude of displacement of the preview marker at each frame, gives the sensation of scraping a pointer along a 3D surface and let’s you “feel” a 3D surface.

![Image](https://cdn-media-1.freecodecamp.org/images/l7GMZUOcwkxV8lsIvnS1xRLPwOOQhNGWl08K)

Here’s a code example of grazing in Unity:

```
if (distanceChange >= 0.1 && distanceChange < 0.2) 
{
    iOSHapticFeedback.Instance.Trigger(Impact_Light);
}
else if (distanceChange >= 0.2 && distanceChange < 0.4) 
{
    iOSHapticFeedback.Instance.Trigger(Impact_Medium);
}
else if (distanceChange >= 0.4)
{
    iOSHapticFeedback.Instance.Trigger(Impact_Heavy);
}
```

#### 3. FPS gun recoil or explosions

This is by far the most fun example of haptic feedback. When building a first person shooter in AR, your phone is the display as well as the weapon. A great way to simulate a gun shot is a simple “Impact Heavy”, which produces a single bump or a “Notification Failure”, which creates a double bump that feels a lot like a gun recoil. Of course the example below is a laser weapon but, hey, this isn’t meant to be too realistic remember?

![Image](https://cdn-media-1.freecodecamp.org/images/6AOfjrGjmc9pSjmaTVQ-88VW7h92isqHEnfz)

#### 4. Collision with controller tip

In VR apps like [Oculus Medium](https://www.oculus.com/medium/) or [Tilt Brush](https://www.tiltbrush.com/), one of the handheld controllers serves as a brush tip that the user moves around to draw in 3D space. I’ve spent hours painting in Tilt Brush and so naturally I have tried really hard to mimic this experience with ARKit.

The trouble is that creating an accurate drawing experience on mobile becomes really difficult. You lose the sense of depth when your phone is both the display and the controller. One of the hardest things in 3D drawing apps on mobile is knowing where your brush tip is relative to the other 3D objects in the scene.

**And, again, haptics was the answer.** We found that one way to give users a sense of depth is to imagine the brush is actually a cane you can use to hit 3D objects that are already in scene. Providing haptic feedback to let users know whether the brush tip is in contact with any existing objects in the scene lets users accurately pin point their brush in 3D space.

![Image](https://cdn-media-1.freecodecamp.org/images/BN9Hp8CqQrX7jHi0jXsy36SRCjSQJqbC4rU-)
_Sensing brush tip collisions_

#### 5. Re-localization snap in Persistent AR Apps.

At [Placenote](https://placenote.com) , we primarily build Persistent AR, or AR Cloud, apps. The core functionality of these apps is the ability to save AR content **permanently** in a physical place. Users can load it up in the same location every time.

This behaviour is called the **relocalization of a scene.**

![Image](https://cdn-media-1.freecodecamp.org/images/8z3xdAIYFaaEPXbpVxXGAhov8pHtYZOaEPdN)
_Localization snapping into place_

In order to relocalize an AR scene, a user must first point their phone’s camera to the real world, and then wait until the camera detects its location.

With Placenote, relocalization happens almost instantaneously but it all happens internally. Hence we need to design a way to notify the user of a successful relocalization. The visual cues might be enough, as seen in the GIF above. But a more subtle indication is to provide a haptic “Impact Light” to suggest that you have snapped into place in the real world.

### **How to add haptics to your ARKit project**

If you’re working with **Swift** for Native iOS ARKit development, [check out this tutorial](https://www.appcoda.com/haptic-feedback/) on implementing haptic feedback in Native apps.

If you’re working with **Unity,** my favorite package so far is the [**iOS Haptic Feedback Package**](https://assetstore.unity.com/packages/tools/integration/ios-haptic-feedback-73225) on the **Unity Asset Store**. It’s $5 but well worth it because Unity’s built in function [Handheld.Vibrate()](https://docs.unity3d.com/ScriptReference/Handheld.Vibrate.html) doesn’t actually expose the new iOS Taptic Engine functions!

The iOS Haptic Feedback Package provides a simple Prefab and Scripts to add all 7 types of haptic feedback into your app. You can get it from the Asset Store link here:

### **Things to watch out for**

As with any design tool, here’s a few things to watch out for when incorporating haptics in your mobile AR app.

#### **Using haptics too much can mess up ARKit tracking**

Test the impact of haptics on your AR session. Since ARKit relies on inertial sensing to track the phone’s motion, adding too many vibrations during an ARKit session can throw off tracking slightly.

#### **Using haptics too much can overheat the device**

Haptics is, after all, a physical movement of your mobile device and naturally tends to use more energy. Use this sparingly to ensure your phone doesn’t overheat or run out of battery too fast.

#### **Too much haptic feedback might confuse and desensitize your user**

This is true for any haptic mechanism. Don’t overdo it. Specifically, don’t use it without a clear understanding of why haptic feedback is necessary for the action your user is performing. The danger of overuse is that your user gets confused by it and therefore gets desensitized to your feedback.

And that’s it! I hope this article has given you a helpful dose of design ideas and convinced you to venture into the world of mobile AR haptics. We’ve really enjoyed exploring the different ways we could simulate touch sensations in mobile AR and if you have any more ideas we would love to talk to you about it. If you’re interested in trying out any of our code examples for mobile AR haptics, send me an email at **neil [at] placenote.com**.

If you’re interested in Persistent AR apps or what we do at Placenote, message us on twitter, or check out [**Placenote.com**](https://placenote.com)

![Image](https://cdn-media-1.freecodecamp.org/images/Gn8g8nxE5b5L2zv-C-1aDXCRS1RuigcRudig)

