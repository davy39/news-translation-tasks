---
title: How I used (computer) SCIENCE! to deal with more than a thousand Lego pieces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T17:07:47.000Z'
originalURL: https://freecodecamp.org/news/using-computer-science-to-deal-with-more-than-a-thousand-lego-pieces-439a2d5a3278
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nnr2BTzLiLncURCANSAOqQ.png
tags:
- name: Computer Science
  slug: computer-science
- name: Life lessons
  slug: life-lessons
- name: play
  slug: play
- name: 'Science '
  slug: science
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eumir Gaspar

  Most kids absolutely LOVE Legos. My son has been playing with the Duplo ones, but
  we have since recently “upgraded” him to the normal ones. Since we didn’t have a
  collection of regular legos yet, we opted to just inherit someone else’...'
---

By Eumir Gaspar

Most kids absolutely LOVE [Legos](https://www.lego.com). My son has been playing with the [Duplo](https://www.lego.com/en-au/themes/duplo) ones, but we have since recently “upgraded” him to the normal ones. Since we didn’t have a collection of regular legos yet, we opted to just inherit someone else’s. We finally got our break when we found someone selling off their kids’ Lego collection since they were too old for them.

![Image](https://cdn-media-1.freecodecamp.org/images/LqBNo6G6BJtK7N1F6MwlWi-nSgAhrLj70NWH)
_This is just half of the collection. Half was already sorted by colours, but these weren’t._

Since we had just gotten a payload of more than a thousand pieces, we now had to sort them by colour just to organise them. I sure wasn’t going [to sort them by part or catalogue them](http://brickarchitect.com/guide/bricks/more/), since that would have taken forever.

So given the insurmountable task, we then decided to get into it. We started sorting by picking up all the green bricks and collecting them in a basin for washing. Yep, this was a very old collection, so it was very dusty.

The initial plan of attack was this:

* I sort the bricks and my wife cleans them and the shelves included. Yes the deal included 3 shelves, 9 boxes, 1 Lego bag (in the photo) and 1 Lego head in addition to probably five to ten thousand pieces
* We then pack them away — easy, right?

This sounded like a good plan, until I realised that sorting by colour the way I was doing it was too slow. I was only picking up one colour at a time. I’d probably only sorted about 30 bricks and it had taken me five minutes. Imagine how long it would have taken for me to finish with the other colours like black, grey, red and blue!

So I had to rethink my plan. I was joking around with a couple of friends who then mentioned I was probably doing [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort), which was one of the slowest sorting algorithms our there (yes there are some other slower algorithms!). I laughed at the joke, then realised I might be able to use my computer science knowledge here — at least what’s left of it! Uni was ages ago, so I knew I’d have to improvise.

### Enter horizontal scaling

I told everyone to stop what they were doing and help me sort out the bag. This meant that now there were more people sorting, so I basically [scaled horizontally](https://en.wikipedia.org/wiki/Scalability#Horizontal_and_vertical_scaling) by adding more resources to finish the job.

As a web developer, I have seen this as a common solution to a problem with server load.

When your server is overloaded by a lot of incoming traffic, you usually have two options: vertical or horizontal scaling.

Vertical scaling means you basically add more power to your server. For example, if you’re using AWS, instead of having a `t2.micro` which only has 1 CPU and 1GB of RAM, you upgrade it to a `t2.xlarge` which has 4 CPUs and 16GB of RAM.

![Image](https://cdn-media-1.freecodecamp.org/images/9DhR1m-V-piFE7y0m1-L-8notdcAfY6VLeCP)
_[The Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/" rel="noopener" target="_blank" title=")_

Horizontal scaling means you just add more resources. So, instead of upgrading your single`t2.micro` instance, you add 5 more to accommodate the load.

Both have their use cases, but for this specific instance, horizontal scaling was the solution.

I mean, I wouldn’t have been able to vertically scale myself by adding more brain power, so the only choice was to horizontally scale by adding more people.

After five minutes of sorting, I noticed that we did make some sort of progress. It wasn’t enough for me though. Time was passing and I was getting tired. We needed to make it faster!

### Divide and conquer algorithm

I had a think. There were three of us with a large bag full of bricks in front of us. I estimated it to be about two thousand pieces at this point. And while we had made some progress in the last five minutes, we were still looking at hours of sorting.

I have since then changed my initial technique of just looking for green blocks. Instead, I was having a quick look at which colour looked like the majority, and getting as many as I could with my hand. After putting the bricks in their appropriate colour basket, I looked at the pile again and picked the “majority” again. It usually changed, since after getting a bunch of say, reds, it would have fewer reds. The next majority would be blue or green, for example.

This was looking good. But after analysing it, I was basically looking at two thousand pieces, getting the maximum count of a colour, getting that colour and subtracting it from the pile. My processing was slow, because how do you actually get the majority without counting or estimating?

Since I was taking too much cognitive load, I was slowing down. So I stopped looking at the colour with the most bricks and just picked a random colour every time I dumped the handful of bricks I had just collected. This sped up my processing a little, but I thought we could still improve.

So, [divide and conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) it was. In CS terms, this meant an algorithm that broke down a huge problem into smaller bits so they were simple enough to solve in a faster time.

Let’s say your site accepts user uploaded zip files with photos and processes them. If your server accepted the zip file, unzipped it, and processed it the minute you uploaded it, everyone else would be waiting for it to finish. Sure you can horizontally or vertically scale your server, but the wait time is unnecessary. Also, what happens when a user uploads a zip file with 100 photos in it?

You can solve this by using a divide and conquer technique instead. First off, you delegate the processing to a delayed job infrastructure like Rails’ [ActiveJob](http://guides.rubyonrails.org/active_job_basics.html). Or if you’re not using Rails, [Sidekiq](https://github.com/mperham/sidekiq). Still, that job would take a long time if it was a 100 photos, and there would be the possibility of your worker dying from the workload.

One solution would be to have a job that unzips it, **and then** enqueues each of the photos to be processed as a separate job. Now instead of your worker having to process 100 photos by itself, it then puts 100 tiny jobs of processing single photos in the queue, which can then be picked up by other workers.

With that in mind, I made a factory line deal with my son: he had to get a handful (or two) of bricks from the bag and dump them into my corner. That meant I only had about 50 bricks to sort which was easier and faster — mainly because by this point, I knew the colour with the most bricks: grey.

![Image](https://cdn-media-1.freecodecamp.org/images/nfwkLNviXS9NJzYYvlZLwoK2Ultncxb7cyoV)
_The most common block colour was grey._

So what if I knew it was grey? Well, that meant that I only had to pick all the red, green, yellow, blue, black and white bricks. When I was left with grey, I dumped the remaining bricks into the grey box — that saved me one less colour to sort that I would not have been able to do on a larger scale.

#### An hour later …

All done! Now we just had to clean them. The initial plan was:

* Dump a box of colours into a basin.
* Wash with water and soap
* Dry

What was the problem here? I’ll give you a guess.

Still there? Okay. If we washed with water and soap, that meant we had to rinse the soap off — which meant we had to wash it twice! No way! So I decided not to add soap but just thoroughly wash with warm water.

The modified plan was:

* Dump a box of colours into a basin
* Wash with water thoroughly
* Dry

On to the next problem: drying the Legos.

### Centrifugal force to the rescue!

Initially, we tried drying the pieces with a towel. It wasn’t very effective. Next was to use a hairdryer and blow hot air into the pieces. It was okay, but it still didn’t dry the pieces — we were getting hopeless and almost decided to just lay them all on the floor and let all the water evaporate.

Only, it was autumn so it wouldn’t have been hot enough. So while pondering about how to dry thousands of Lego pieces, I suddenly remembered how I dry salad leaves using a salad spinner. “I wish I could use the salad spinner,” I thought. Then it dawned on me: a [salad spinner](https://en.wikipedia.org/wiki/Salad_spinner) works by using [centrifugal force to separate the water from the leaves](https://en.wikipedia.org/wiki/Centrifugal_force). I could do the same!

I wrapped the lego pieces into a towel and secured them by turning the towel into a giant candy wrapper. I stepped on one end of the towel, pulled the other end as tight as I could and started spinning the towel.

What do you know — it actually worked! I could see the towel suddenly become wet as the water from the pieces flew out of them and into the towel. SCIENCE!

![Image](https://cdn-media-1.freecodecamp.org/images/HEp6MVkDlD9fjO7zFMgzQ0Wj1Xwpl4vcfFi1)
_SCIENCE!_

The Legos weren’t completely dry, of course, so I still had to use the hairdryer to help the remaining droplets evaporate. But that was all right — the hard part was over.

I never thought I’d use my stock CS knowledge for something like sorting Legos. In any case, it was a good and fun experience scaling horizontally, using a divide and conquer strategy, and even bringing out centrifugal force to organise my son’s newly inherited Lego collection. I don’t look forward to the day he jumbles them all up and we have to sort them again, though!

