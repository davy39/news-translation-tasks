---
title: 'Hardware fundamentals: how pull-down and pull-up resistors work'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-17T19:40:27.000Z'
originalURL: https://freecodecamp.org/news/a-simple-explanation-of-pull-down-and-pull-up-resistors-660b308f116a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SMTqmqkvw4LnRckc2Wj9RQ.jpeg
tags:
- name: arduino
  slug: arduino
- name: hardware
  slug: hardware
- name: Internet of Things
  slug: internet-of-things
- name: Makers
  slug: makers
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Taron Foxworth

  If you’ve ever wired up a button to an Arduino, you’ve come across this diagram:


  At first, this can be confusing. My first thoughts: “Why do I need a resistor? I
  just want to it to tell me whether the button is being pressed.”

  Afte...'
---

By Taron Foxworth

If you’ve ever wired up a button to an Arduino, you’ve come across this diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/5z3GVJwnEtxRQZnrIeMa6806A0l45ZDHoLLc)

At first, this can be confusing. My first thoughts: “Why do I need a resistor? I just want to it to tell me whether the button is being pressed.”

After a lot of reading, there wasn’t a simple explanation.

### What’s going on here

![Image](https://cdn-media-1.freecodecamp.org/images/lnCBI4aQPD72ryakAoXRZOOIscOKzO1TN8T-)
_Diagram 1_

In that button — AKA a switch—the wires are shaped in the form of an “H”. But the middle isn’t connected — or the circuit isn’t connected — until we press the button.

In reality, we want to read from the Arduino a `0` when nothing is connected and a `1` when the button is pressed.

On the Arduino, this is called General Purpose Input Output ([GPIO](https://en.wikipedia.org/wiki/General-purpose_input/output)).

So, we can do something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/ei-WY10bPEXDJh5eHRZ8VW0K1Xp0E-fWPQz5)
_Diagram 2_

We connect positive (5v, 3.3V, or VCC) to the left side of the circuit.

Now, when the button is pressed, the GPIO will read a `1`, and all is good.

![Image](https://cdn-media-1.freecodecamp.org/images/WjBnoryrJcaJusAFgohNgpnKrR0mKXYI7fmd)
_Diagram 3_

Well, no. Let’s take a look at Diagram 2 again:

![Image](https://cdn-media-1.freecodecamp.org/images/1T7hhKBigZliDdNhgut-kKK8KMmgId1jEAEv)
_Diagram 2_

We wanted a `0` when nothing is connected, but how can you guarantee this? Currently, there is no way to guarantee the GPIO to be `0`.

There is also electromagnetic frequencies in the air that could draw your GPIO to `0` or `1`. It could even fluctuate between the two! This way, we can’t be positive it’s a `0` (I’m so bad at puns). This is also known as a logical `0`.

One way to get a logical `0` is to tie the pin to Ground:

![Image](https://cdn-media-1.freecodecamp.org/images/mZLL1wlSMz6ReTNeJZDAQMaIOVnkOTrg5qqY)

Yay! So, now it’s a guaranteed logical zero. While pushing the button, it’s going to be `1` now. Right?

Well, No.

![Image](https://cdn-media-1.freecodecamp.org/images/sMUiXkmyybe-DrcMuYHb0IqpU3FFLtTYm-uy)

You just created a [short circuit](https://en.wikipedia.org/wiki/Short_circuit). ?

This is where the resistor comes in. To avoid a short circuit, we need to add resistance to our circuit. The resistor keeps things under control.

![Image](https://cdn-media-1.freecodecamp.org/images/T3HTmawK4YN37wNqYke-QQdh5EVmFnNY8nec)

[Electricity will take the path of least resistance.](http://ecmweb.com/content/path-least-resistance) Your GPIO will now register a `1` when the button is pressed. Like so:

![Image](https://cdn-media-1.freecodecamp.org/images/yLtF3UnfFhhhZ4Kjdqg81d4MvXqVDsYuCclh)

![Image](https://cdn-media-1.freecodecamp.org/images/msnI0gnXpKvs5h6JuTVHExkeAWJuzxyl7J2x)

Woo Hoo! Now we’re working with something.

Now let’s look at the opposite: pull-up resistors. It’s the same thing but in reverse. While the button is not pressed, the GPIO will register a `1`. When you pressed the button, the GPIO will be `0`.

While not pressed, we have the GPIO connected to positive ( VCC ). So, any current that is there will be pulled-up so that the GPIO registers a logical `1`.

![Image](https://cdn-media-1.freecodecamp.org/images/zUGnUEh9axrnFyaWOvkUNt1B5uCZxQBewETh)

It’s important to note here that, electricity always wants to go to Ground. So, when we press the button, the current that’s flowing will flow to Ground. Thus, any current that would have been going to the GPIO goes with it, leaving the GPIO at a logical `0`.

![Image](https://cdn-media-1.freecodecamp.org/images/4NW0bqGqmZbUolmRv4LObF5qR8fccQ1z9zl0)

? The End.

#### Why did I write this?

I joined [Losant](https://losant.com) in September of 2016 with no hardware experience. Every single hardware starter kit gives you a button with no explanation of this concept. Hopefully, this helps your light bulb go off too. ?

This only scratched the surface. If you want to dig deeper, check out these resources:

[**Pull-up Resistors - learn.sparkfun.com**](https://learn.sparkfun.com/tutorials/pull-up-resistors)  
[_Another thing to point out is that the larger the resistance for the pull-up, the slower the pin is to respond to…_learn.sparkfun.com](https://learn.sparkfun.com/tutorials/pull-up-resistors)

I love feedback. So, please let me know if this could be improved. **If I totally missed the ball on this, [let me know](http://twitter.com/anaptfox)!** I would love to make it better for others.

