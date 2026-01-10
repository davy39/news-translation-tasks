---
title: The race is on for artificial intelligence. Here’s who is winning.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-08T18:23:42.000Z'
originalURL: https://freecodecamp.org/news/the-race-is-on-for-artificial-intelligence-heres-who-is-winning-f7dad96f1d33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1cqiEqRqDuvvfvsO1M68qw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Terren Peterson

  On Saturday, Louisville, Kentucky hosted the 143rd running of the Kentucky Derby.
  It was a spectacle where more than 150k people watched in person. Millions more
  followed on television and streaming media. The winner received a $1....'
---

By Terren Peterson

On Saturday, Louisville, Kentucky hosted the 143rd running of the [Kentucky Derby](https://www.kentuckyderby.com/). It was a spectacle where more than 150k people watched in person. Millions more followed on television and streaming media. The winner received a $1.4 million prize, and the opportunity for more winnings in later races this year.

A bigger race is raging within the technology sector around who can commoditize machine learning as a service. Prebuilt machine learning models are worth billions of dollars. This competition pits the largest technology companies on the planet.

Events such as the Kentucky Derby actually have many races going on during the same day. The race to dominate machine learning is the same. For this article, I’m going to just focus on how the race for image recognition is shaping up.

### The Cloud Contenders

Right now there are options from each of the major Public Cloud vendors. Amazon, Google, and Microsoft get a prime position based on their storage hosting services. Their offerings will determine the market direction. Image recognition may become a feature built into big cloud-based image storage systems. This move would eliminate prebuilt models as a separate product.

#### Testing out the current offerings

To “race” the providers against one another, I used the photo below from [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/7/7b/Horseracing_Churchill_Downs.jpg). To make the article more readable, I reduced the precision on each of the responses below to three digits.

![Image](https://cdn-media-1.freecodecamp.org/images/K27Q2AZXkFG6E01SPc-Y8Y9WYr29aofhpMHR)

#### Amazon

Amazon has the largest Public Cloud footprint in the industry. Six months ago they released their MVP of [Rekognition.](https://aws.amazon.com/rekognition/) This service builds on their Cloud platform as it integrates into S3 and Lambda. Here is what their models determine from the race photo.

```
[{’Confidence’: 98.0, ’Name’: ’Animal’},{’Confidence’: 98.0, ’Name’: ’Horse’},{’Confidence’: 98.0, ’Name’: ’Mammal’},{’Confidence’: 90.8, ’Name’: ’Equestrian’},{’Confidence’: 90.8, ’Name’: ’Person’},{’Confidence’: 52.7, ’Name’: ’Colt Horse’}]
```

#### Google

Google has a large Cloud business, including object storage. Their history with image recognition in search is also a massive advantage. Using their [Cloud Vision API](https://cloud.google.com/vision/) provides a thorough response on the race image.

```
[{ "description": "horse", "score": 0.937 },{ "description": "western riding", "score": 0.889 },{ "description": "jockey", "score": 0.881 },{ "description": "racing", "score": 0.861 },{ "description": "stallion", "score": 0.810},{ "description": "mare", "score": 0.810 },{ "description": "western pleasure", "score": 0.806 },{  "description": "sports", "score": 0.776 },{  "description": "horse racing", "score": 0.775 },{  "description": "english riding", "score": 0.731 },{  "description": "horse trainer", "score": 0.722 },{  "description": "equestrian sport", "score": 0.708 },{  "description": "equestrianism", "score": 0.705 },{  "description": "animal sports", "score": 0.685 },{  "description": "barrel racing", "score": 0.648},{  "description": "eventing", "score": 0.614},{  "description": "horse like mammal", "score": 0.590},{  "description": "reining", "score": 0.546 }]
```

Google goes even further by adding in text recognition. When scanning the image, it translated the text in the scoreboard. See the yellow boxes in the top left of the image below.

![Image](https://cdn-media-1.freecodecamp.org/images/VShdHXElPgOiLBHMPRVbNcbadHj70Getdkgj)

Google translates this information into a machine readable format (JSON). This is a powerful feature that others don’t offer yet.

#### Microsoft

Microsoft also has the combination of a large Cloud and Search business. Their offering has been on the market for more than a year. Their [Cloud Vision API](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api) recognized the image, and provided the following results.

```
[ { “name”: “grass”, “confidence”: 0.999 },{ “name”: “fence”, “confidence”: 0.999 },{ “name”: “outdoor”, “confidence”: 0.995 },{ “name”: “horse”, “confidence”: 0.985 },{ “name”: “ground”, “confidence”: 0.974 },{ “name”: “sport”, “confidence”: 0.821 },{ “name”: “horse racing”, “confidence”: 0.519 }]
```

### The Long-Shots

This race has more entrants than the three major Public Cloud providers. IBM has Watson, and strong capabilities in AI. They have enabled this capability within [BlueMix](https://visual-recognition-demo.mybluemix.net/). Here’s what I got when attempting to use the public demo using the photo.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

There are limitations with this service as there are restrictions on size. This may be a usability gap the deters customers. I found a [similar photo](https://upload.wikimedia.org/wikipedia/commons/6/63/Horse-racing-4.jpg) on Wikipedia that was within the 2MB threshold. The quality of the recognition was similar to the others.

```
[ { "class": "horse racing", "score": 0.922 },{ "class": "racing", "score": 0.928 },{ "class": "sport", "score": 0.928 },{ "class": "jockey (horse rider)", "score": 0.622 },{ "class": "traveler", "score": 0.622 },{ "class": "person", "score": 0.622 },{ "class": "racehorse", "score": 0.53 },{ "class": "mammal", "score": 0.53 },{ "class": "animal", "score": 0.53 },{ "class": "green color", "score": 0.876 }]
```

Start-ups provide creative alternatives in this race. An example is [Clarifai](https://www.clarifai.com/demo) that [raised $30M](https://techcrunch.com/2016/10/25/clarifai-raises-30m-to-give-developers-visual-search-capabilities/) last year. Their API highlighted strong recognition using the same image as the tech giants.

```
horse, 0.999equine, 0.992race, 0.990track, 0.989fast, 0.984jockey, 0.983thoroughbred, 0.981competition, 0.966gambling, 0.951filly, 0.942mare, 0.936turf, 0.924whip, 0.902best, 0.897stallion, 0.882athlete, 0.869saddle, 0.865racehorse, 0.864rider, 0.864blinker, 0.858
```

This highlights the potential for a newcomer to break into this race. The startup could ride the rails of an existing Cloud hosting provider, giving it economies of scale.

### Who is the winner?

The race is very competitive, with Google currently in the lead. Software developers integrating image recognition into their digital products are also winners. I recently built an Alexa game that uses it to play [scavenger hunt](https://medium.freecodecamp.com/how-to-make-scavenger-hunts-more-fun-with-artificial-intelligence-74a184f3db33). This was done with just a few lines of code, and no effort to train models.

The current price point is around $1/thousand images. At this level, image recognition will be incorporated into many different products. The race to become the most consumed service is on!

