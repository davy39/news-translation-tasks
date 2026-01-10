---
title: Does Data Compression matter on a Quantum Internet?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-28T15:37:24.000Z'
originalURL: https://freecodecamp.org/news/does-data-compression-matter-on-a-quantum-internet-f6b986473c1c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jB_VRVuG5z8Dtp2i4N1o9g.png
tags:
- name: data compression
  slug: data-compression
- name: General Programming
  slug: programming
- name: quantum computing
  slug: quantum-computing
- name: 'Science '
  slug: science
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Colt McAnlis

  Disclaimer: This is a hypothetical think piece. It is a personal opinion and doesn’t
  represent the opinion of any of the companies (or secret societies) I may (..or
  may not) be involved with. If you tear a hole through space-time afte...'
---

By Colt McAnlis

_Disclaimer: This is a hypothetical think piece. It is a personal opinion and doesn’t represent the opinion of any of the companies (or secret societies) I may (..or may not) be involved with. If you tear a hole through space-time after reading this article… that’s your own fault._

If you haven’t heard, a research team out of China just made a huge leap with respect to realization of using [Quantum Entanglement as a valid communication vessel](http://science.sciencemag.org/cgi/doi/10.1126/science.aan3211). Their process was to use a low-earth satellite to create a pair of entangled photons and then send them to locations very far apart from each other. Even at never-before-done distances, the photons retained their entanglement, which has set the internet a buzz about the future of communication, and when the new quantum internet will happen.

Now, looking at the math, **I’m still a bit dubious that quantum entanglement** could be viably used for communication. This math person [explains](https://www.forbes.com/sites/chadorzel/2016/05/04/the-real-reasons-quantum-entanglement-doesnt-allow-faster-than-light-communication/#1c0c3f153a1e) it a [bit better than](https://medium.com/starts-with-a-bang/ask-ethan-can-we-use-quantum-entanglement-to-communicate-faster-than-light-e0d7097c0322) I ever could. However, there’s lots of people hypothesizing that this is the first steps in a new quantum internet where things like [Entanglement Swapping](http://spectrum.ieee.org/telecom/security/two-steps-closer-to-a-quantum-internet) and [Twisted Light](https://en.wikipedia.org/wiki/Orbital_angular_momentum_of_light) could bridge those gaps.

**Then let’s propose a thought experiment**: let’s assume there’s future where an internet exists, whose technology is based on quantum entanglement. This means that data can be transmitted between two locations, at close to speed-of-light without a physical connecting medium between the locations.

In such a world, does data compression matter any more?

### A small idea on how a QE internet would work

We have to assume that due to current technology, the first realization of a QE Internet (QEI) would be very similar to the telegraph systems of the past. The cost to maintain and run these early QEI sites would limit their availability, meaning that communication could only occur between a handful of sites.

These sites would require two primary features:

1. A non-centralized system which can distribute entangled photon pairs to the sites (a low-orbit satellite, for example).
2. A recording system which logs the results of the entanglement tests and can store / retrieve them.

![Image](https://cdn-media-1.freecodecamp.org/images/Xp0h0wKzejEnv3nQ4yA-OAbVQ0AZU064giIv)

#2 would be most likely built on today’s modern technology. So you can expect a situation where a billion photon pairs are sent to a site, and sampled in unison, and stored as binary data at the location.

From that point, the data would be most likely distributed to it’s final destination using more conventional methods (e.g. fiber connection).

### Limitations of a first generation QEI

Obviously, we still end up with some data-based bottlenecks here:

1. There is a physical limit to how many entangled pairs can be stored at a site, thus limiting it’s total bandwidth.
2. There is a physical limit to the speed in which entangled pairs can be sent from the distributor to the sites on a regular basis, thus limiting total system bandwidth.
3. Environmental factors will cause loss of data in the transfer of photons to the sites from the distributor system. Thus, there will be a need for redundancy in the process, limiting total system bandwidth.

When observing the above, you can quickly seen that the overall bandwidth of a QEI would be limited by the above systems, regardless of the ability for information to travel between sites through quantum means. So obviously, reducing the size of the data being sent through the sites will be important, but will today’s data compression algorithms make sense?

### Data compression for a QEI

There’s a few definitions of “data” which represents it as a physical entity, and as the (potential) realization of a Quantum Internet is realized, the need for photon transferal makes this concept even more real.

In fact, that may be the largest ramification of a quantum entangled internet: your data now has a very physical manifestation and cost involved with it.

So it’s obvious that data compression, as a science, will still be needed in a QEI future, but the real question we should be asking ourselves is: **Are today’s compression algorithms good enough to support a quantum internet?**

My opinion? Not even close.

![Image](https://cdn-media-1.freecodecamp.org/images/muYjkNnMLxY6BjdD-TiW37VflNvJOFyizCaS)

As explained in “[Understanding Compression](https://www.amazon.com/Understanding-Compression-Data-Modern-Developers/dp/1491961538)” today’s systems are still grounded around Shannon’s basic architecture of ‘_the most frequent symbol gets the smallest bits._’ There’s a lot of power in this process, but until we move out of symbol space, and start gaining the computational power to handle compression entirely in bit-vector space, [we’re going to be leaving a lot of information on the table](http://ieeexplore.ieee.org/abstract/document/1054929/). (But _that’s my own unpopular opinion..._)

Let’s look beyond that. Are there potential systems where, rather than applying [Brotli](https://github.com/google/brotli) to a data set, we instead can apply in to entangled photons directly? Will we start talking about algorithms to do diff’s against the photons on a site, and the data being transmitted, so we can reduce the number of updated pairs? What happens when we start thinking in terms of [qubits](https://en.wikipedia.org/wiki/Qubit), rather than just bits? Do we have to start thinking about LZ encoding in 8 dimensional space?

Obviously, the realization and standardization of Quantum Computing will create a massive technological shift in how our world works. And I’ve got every reason to believe that Data Compression will be right there, too.

