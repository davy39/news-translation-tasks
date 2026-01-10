---
title: It’s easy to trick your phone’s fingerprint scanner. Here’s how we should fix
  it.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-24T15:36:53.000Z'
originalURL: https://freecodecamp.org/news/it-is-easy-to-trick-the-mobile-phones-fingerprint-scanner-d8d7f509d128
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fPDbcBXDvkEgZ5mp9xfF8A.jpeg
tags:
- name: Android
  slug: android
- name: Apple
  slug: apple
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nikhil Dwivedi

  Early last week, I was setting up fingerprint sensors on my new iPhone. That’s when
  my brother, @Prateek , came up with an idea to test these mobile fingerprint sensors.

  The test was to scan his finger along with mine at the time of...'
---

By Nikhil Dwivedi

Early last week, I was setting up fingerprint sensors on my new iPhone. That’s when my brother, [_@Prateek_](https://twitter.com/prateekdwv) , came up with an idea to test these mobile fingerprint sensors.

The test was to scan his finger along with mine at the time of fingerprint setup. You know how these devices ask you to lift and then rest your finger multiple times to capture all possible angles. So we did it — got his finger scanned a few times when the phone was expecting me to lift and rest only my finger.

![Image](https://cdn-media-1.freecodecamp.org/images/ihb6oUoreF0lZP3x6FOX26g5xcBIp7uwywOt)
_Image showing iPhone finger scan setup_

To my astonishment, we were successful in bluffing the phone. Setup was complete, and now both of us could use our finger to unlock the phone. This is how the settings looked — just one finger configured, and both of us could unlock the phone.

![Image](https://cdn-media-1.freecodecamp.org/images/ZntDoKdtDzZSxQuK1MKHICDLsmt6ieOiDvuZ)
_iPhone Settings Page showing just one finger configured_

The thought crept into our brains: is this some sort of a bug, or what? For now, this was the time for a fun exercise — to try it out with all other phones that support fingerprint sensing.

So we began with various Android phones, a few with stock ROM and others with custom operating systems from a third party like Micromax, Lenovo, and Xiaomi. The result was same for all. We could each use our finger to unlock the same phone while only one finger was set up.

### First, let’s understand how these mobile fingerprint scanners work

Sticking to the point, there are two popular and core technologies behind fingerprint scanning in mobile phones.

**Optical Scanner** — this technique uses an optical image to capture various images of your finger. A kind of high precision camera and few LEDs do the job here. The software then compares these two-dimensional images with the image taken from the scanned finger.

Since this is essentially just an image that is compared, these scanners are easy to deceive. An image of a finger printed using a high DPI printer is enough to fool these types of scanners.

**Capacitor scanner** — here an array of capacitors capture the pattern from the scanned image. A complex electric circuit beneath captures the data and that is used to compare the scanned finger.

This technique is far more secure and is difficult to deceive. A high definition image of a finger cannot be used to unlock the phone. The Samsung Galaxy S8 phone claims it uses this technique.

### _Now time for the debate: is it right or not?_

At first, when you see this happening, you can tell something unusual is going on. To keep your fingerprint scanner secure, the following components are important:

* _Scanning Technique_— hardware used to scan the finger and extract data/patterns from it.
* _Storage_ — Database where the data/pattern of the fingerprint is stored.
* _Algorithm_ — that is used to store and compare the scanned pattern.

![Image](https://cdn-media-1.freecodecamp.org/images/ucfJ-wZD8S9EGf7ptKgFV6bY8FvogXEamMby)
_General Architecture of Mobile Fingerprint Scanner_

For overall security, recording fingerprint is as important as referring database for verification. There seems a flaw and inefficiency in the way fingerprints are stored.

Looking at the case above, it appears that various fingerprint impressions gathered at the time of setup are stored as an independent set of data. When you scan a finger to unlock the device, the scan is compared against an array of the binary representation of fingers that were scanned at the time of setup. _Possibly, this is how we were able to trick the phone by scanning another person’s finger at the time of setup._

![Image](https://cdn-media-1.freecodecamp.org/images/pJFbTm37qw0toUb4pfJO2v7FuYAGXuYSozuz)
_Representation — An array of fingerprints, stored at time of setup. [source](http://www.mdpi.com/1424-8220/10/5/4206/htm" rel="noopener" target="_blank" title=")_

There appears to be a conceptual and fundamental problem in how the system currently works.

I can not claim any use case where this could lead to a security-gap. But since the adaption of fingerprint-based authentication is increasing rapidly, and its usage has gone beyond just unlocking your device, it makes sense to improve the technology to bridge the gap.

### So, what next?

At the time of setup, successive scans of the finger could be compared with each other to ensure that all the recorded scans were of the same finger. It is obvious to have some percentage of overlap between various scans. Such a thing would have stopped [Prateek Dwivedi](https://www.freecodecamp.org/news/it-is-easy-to-trick-the-mobile-phones-fingerprint-scanner-d8d7f509d128/undefined) from scanning his finger when I was trying to setup the phone. _This would have secured the way fingerprints are captured at the time of setup._

![Image](https://cdn-media-1.freecodecamp.org/images/hLsbzoXZyPNqGAclK5EVK1qwl87iZmL2XJJL)
_Some overlap between two successive scans_

Retrieval could be made more secure by not comparing the scan to unlock the device with just one of the pre-stored scans. Ideally, the scan will compare to a high degree with one of the stored representations, and it will also compare to all other scans to some degree. Instead of relying on just one optimal match, we should score the match based on a comparison from all the representations. Accumulative percentage of comparison should be considered to authenticate.

### Conclusion

To conclude, as I pointed out in my [previous blog](https://medium.com/@niks.dwivedi/biometric-identification-usage-in-finance-mobile-applications-11b15c8d0b88) — “[Bio-metric Identification & usage in Banking Mobile Applications](https://medium.com/@niks.dwivedi/biometric-identification-usage-in-finance-mobile-applications-11b15c8d0b88):”

The bio-metric authentication is not yet secure enough. Recently, we have seen an inclination and shift towards using these techniques for payments and financial transactions as well. The rise of mobile phones and IoT devices has added to the adaption of bio-metric authentication techniques. It is time to think more about making bio-metric authentication technology more secure and difficult to compromise.

_Follow me on medium — [Nikhil Dwivedi](https://www.freecodecamp.org/news/it-is-easy-to-trick-the-mobile-phones-fingerprint-scanner-d8d7f509d128/undefined)._

_My twitter handle is — [@Niks_Dwivedi](https://twitter.com/Niks_Dwivedi)_

