---
title: How to Speed Up Your Old Laptop - Using Stuff You Have Lying Around Your House
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-28T23:21:47.000Z'
originalURL: https://freecodecamp.org/news/speed-up-old-laptop
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/20191029_080609.jpg
tags:
- name: performance
  slug: performance
seo_title: null
seo_desc: 'By Jackson Bates

  I''m extremely proud of my laptop. It''s about 7 years old, but was pretty well
  equipped in its heyday, with a core i7 processor and 6GB RAM it was excellent for
  everything I was using it for. It''s also survived many knocks and drops -...'
---

By Jackson Bates

I'm extremely proud of my laptop. It's about 7 years old, but was pretty well equipped in its heyday, with a core i7 processor and 6GB RAM it was excellent for everything I was using it for. It's also survived many knocks and drops - I'm pretty sure it's bulletproof.

Recently it's been grinding to a halt whenever I try to have a few Chrome tabs, VSCode and the Slack app open - you know, _everything a developer has open all the time_!

I checked the RAM and CPU usage on my machine and everything was fine. Even though those apps are notoriously resource intensive, a decent CPU and a moderate amount of RAM should have been sufficient.

However, there was one other issue that had been bugging me. The VGA port on the side would get so hot that when I'd absentmindedly rest my fingers on it they'd get slightly scalded.

My CPU was overheating - and as a safety precaution, my computer was throttling itself so as not to meltdown. Sure enough, when I installed some sensor command line utilities on my machine to check the temperature it was reporting that the temperature was high, and dangerously close to critical:

```
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +95.0°C  (high = +87.0°C, crit = +105.0°C)
Core 0:        +95.0°C  (high = +87.0°C, crit = +105.0°C)
Core 1:        +98.0°C  (high = +87.0°C, crit = +105.0°C)
Core 2:        +92.0°C  (high = +87.0°C, crit = +105.0°C)
Core 3:        +91.0°C  (high = +87.0°C, crit = +105.0°C)

```

I have a confession to make: In 7 years of owning this beloved laptop, I have never cleaned it!

![Image](https://www.freecodecamp.org/news/content/images/2019/10/20191029_073715.jpg)
_Your laptop fan is the real MVP, treat it well._

Sure enough, when I opened up the laptop shell, the problem was clear - 7 years of accumulated dust clogging the fan.

So how do you speed up your old laptop? Clean it!

## You will need

* Tools for opening your laptop (in my case just a Phillips Head Jewelers Screwdriver);
* Cleaning Alcohol (I used methylated spirits);
* A small, clean brush; and/or
* A can of compressed air;
* Optional: Thermal paste (OK - you may not have this lying around your house, but it's  [it's cheap](https://www.amazon.com/Arctic-Silver-AS5-3-5G-Thermal-Paste/dp/B0087X728K))

## Method

The basic principle is simple - your CPU is overheating because your heat sink and fan cannot dissipate the heat quickly enough.

We'll do two things - clean the fan, and apply new thermal paste to your CPU to improve heat transfer.

Since every laptop make and model is constructed differently, you'll need to consult your manufacturer's instructions for safely disassembling your machine. Alternatively, seek out videos for your exact make and model. The images and precise method in this post relate to my own ThinkPad E530.

**WARNING: If you are unsure of what you are doing, consider having your laptop professionally serviced. Proceed at your own risk - we're not liable for you frying your laptop or electrocuting yourself!**

### Step 1

Remove your laptop from the power supply, remove the battery, and hold down the power button for about 5 seconds to discharge any residual power.

### Step 2

Remove the casing that houses the CPU, heat sinks and fan. See your manufacturer instructions for this.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/before-1.jpg)
_The inside of a ThinkPad E530_

### Step 3

Unscrew the components you need to service. In my case this meant unscrewing the heat sink and fan. Remember to gently unplug your fan by pulling or prying the plastic connector - don't pull on the wires.

### Step 4

Clean the old thermal paste off of the CPU and heat sink (and any other areas it's previously been applied - such as the GPU in my case). I did this in 2 stages - gently scraping the dried paste from the areas it had bonded to, and then using the cleaning alcohol on a lint free cloth to remove the rest. In the image below, those grey gunky parts on the heat sink are the old thermal paste.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/20191029_074237.jpg)
_The ThinkPad E530 heat sink and fan unit_

### Step 5

Clean any visible dust from the inside of the laptop shell with your brush. Clean the fan thoroughly with your brush, and use your compressed air to blow dust out of the vents. Make sure you are not blowing dust back into the open laptop case!

![Image](https://www.freecodecamp.org/news/content/images/2019/10/20191029_081117.jpg)
_As good as new!_

### Step 6 (Optional)

Apply thermal paste to your processor (and other parts where necessary). A tiny amount is sufficient. I strongly recommend reading the detailed instructions that are provided online by your thermal paste manufacturer. I used [Arctic Silver 5 brand](https://www.amazon.com/Arctic-Silver-AS5-3-5G-Thermal-Paste/dp/B0087X728K).

### Step 7

Put it all back together, remembering to plug the fan back in (confession: I forgot!)

## Results

As soon as I turned my laptop back on it felt snappier. And a quick sensor check confirmed that the small amount of effort was worth it for my poor laptop's sake:

```
coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +45.0°C  (high = +87.0°C, crit = +105.0°C)
Core 0:        +45.0°C  (high = +87.0°C, crit = +105.0°C)
Core 1:        +38.0°C  (high = +87.0°C, crit = +105.0°C)
Core 2:        +43.0°C  (high = +87.0°C, crit = +105.0°C)
Core 3:        +40.0°C  (high = +87.0°C, crit = +105.0°C)

```

The VGA port doesn't burn any more!

---

If you enjoyed this post and avoided toasting your CPU, follow [@JacksonBates](https://twitter.com/JacksonBates) on Twitter for more informal tech related ramblings.

