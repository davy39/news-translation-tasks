---
title: For more realistic FramerJS prototypes, just add data
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-17T02:01:09.000Z'
originalURL: https://freecodecamp.org/news/i-tried-framer-and-i-loved-it-part-2-31fdef35a1e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uTJpHuWyI1Ly0QxpN31zng.jpeg
tags:
- name: Design
  slug: design
- name: prototyping
  slug: prototyping
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Marty Laurita


  “Data! Data! Data! I can’t make bricks without clay!” — Sir Arthur Conan Doyle


  Most interaction prototypes today serve one purpose: to convince your user that
  this prototype is what the “real thing” will look like and feel like.

  In...'
---

By Marty Laurita

> _“Data! Data! Data! I can’t make bricks without clay!”_  
>  _—_ Sir Arthur Conan Doyle

Most interaction prototypes today serve one purpose: to convince your user that this prototype is what the “real thing” will look like and feel like.

In the past, designers have achieved this with fancy user interfaces, animations, and fluid transitions.

But those don’t quite cut it anymore. Users have become jaded to these tricks. They lived through the iPhone era, and now expect a fluid UI to come standard.

So what’s the next frontier then? How can we convince people that a prototype is “real”?

By using real data.

![Image](https://cdn-media-1.freecodecamp.org/images/RBuldGdjUUlgWe4ddyHiOf7CDgkUOkiSfJYx)
_Time to go down the rabbit-hole…_

[FramerJS](http://framerjs.com/) is a powerful code-based framework for building prototypes for your web apps and mobile apps. In this article, I’ll show you how you can use it to build a realistic prototype that features real data.

![Image](https://cdn-media-1.freecodecamp.org/images/LhK7VTU-bltvg4IbuXyskjszjf0G360oaaaL)
_Framer’s Interface, Framerjs.com_

As a rider of the Massachusetts Bay Transportation Authority (MBTA), I have the distinct pleasure of riding a transit system that is over 100 years old.

As you can imagine, the trains aren’t always on time.

I’ve become relatively familiar with Framer, and as such, I decided to try and design an app to solve this problem.

As a designer who has only a whisper of an understanding of code, this was daunting to say the least.

I called up my brother, a talented computer science major at Tufts, and we got down to business.

![Image](https://cdn-media-1.freecodecamp.org/images/YSIqERsQ25SECvWvmzrsCTzSPrJG3pVQOtEB)
_[come hither]_

### Locating our users

The first thing to do was find the user’s location in realtime.

Today’s mobile browsers have this feature built-in.

With two functions, you can get the latitude and longitude of your user.

Then, you can just stick those coordinates into what’s called a [hash table of key value pairs](https://www.google.com/search?q=define+hash+table&oq=define+hash+table&aqs=chrome..69i57j69i60j69i65j69i61j69i60j69i61.2328j0j1&sourceid=chrome&ie=UTF-8). In this table of data, the key might be “dog_breed” and the value might be “Pomeranian.” So now, you can call on that key whenever you need it, and it will return its corresponding value.

Here’s what we ended up with:

```
#get locationgetLocation = () -> print “INSIDE GET LOC” navigator.geolocation.getCurrentPosition(showPosition);
```

```
showPosition = (position) -> print “INSIDE SHOW POS” gpsCoords = { “client_lat”: “#{position.coords.latitude}”, “client_lon”: “#{position.coords.longitude}” }
```

Now that we have the user’s exact location, it’s time for phase II.

### Locating our trains

![Image](https://cdn-media-1.freecodecamp.org/images/YAH7ojN31RC47pIjYoBTrsv3p--ghcZ6a8Ss)
_Where’s that train….Mr. Andersonnnnn?_

Getting the user’s location was the easy part. Now, we need to find and parse the API data from the MBTA.

Unfortunately, this organization is about as organized as any other under-funded government operation.

So, their code was — how should I put this — a little janky. Here’s what it looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/p8p21fIHRxZoFPNjyjz27AQKjy-HYdS0NJPH)
_Kiiind of a jumbled mess._

The data was nested in a combination of arrays and key value pairs. Some of them were data tables with just one entry. It took some time to understand how to pull out the data we needed.

Regardless, once we understood the structure, the idea was to grab the location data from the user’s browser and insert that into the API call to the MBTA. Then the MBTA API would return all data closest to that location.

The first piece of data we wanted was the closest station to the current location:

```
#grab MBTA station datadata = JSON.parse Utils.domLoadDataSync “http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=De_WCTE-gkyYSitBw82YSw&lat=#{gpsCoords["client_lat"]}&lon=#{gpsCoords["client_lon"]}&format=json"  stops = data[“stop”]  stationText.html = null  for i in stops  if i[“parent_station_name”] != “” stationText.html = “The closest station to you is “ + i[“parent_station_name”] + “.”
```

Once we had the data, we then parsed it into something humans can read. We created a string (an English sentence) that said “The closest station to you is” and then tacked the station name on at the end. And Voila! The first step!

![Image](https://cdn-media-1.freecodecamp.org/images/axJpiQsITNU8n7HhoNeGQB4y9jWeoomCU6WI)

It worked like a charm!

Except not in Google Chrome.

We quickly learned that for some strange reason, Google had decided to disable location APIs. Really Google? You don’t have enough billions to give some location data to the little guy?

But anyway, the prototype works great in Safari.

![Image](https://cdn-media-1.freecodecamp.org/images/UZ7MSBeDGnIISe9-xbd0Zennr9YhHEKRicvU)

After celebrating our initial success, we decided to make our lives hard again.

What if we wanted to know not only the nearest station, but also how far the closest train was, where it was coming from, and how many minutes away it was?

Oh boy.

![Image](https://cdn-media-1.freecodecamp.org/images/YEKj7SSCJTSMpITWBp12yrv1zLTc79pHXFuW)
_That “uh-oh” moment._

### More Crazy Data

Now that we had a handle on how the MBTA data jives, we dove into a second API that provides (mostly) accurate train data.

After some finagling, we had something like this:

```
#grab nearest train data data2 = JSON.parse Utils.domLoadDataSync “http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=De_WCTE-gkyYSitBw82YSw&stop=#{i["stop_id"]}&format=json" routes = data2[“”] timeAway = data2[“mode”][0][“route”][0][“direction”][0][“trip”][0][“pre_away”] trainDir = data2[“mode”][0][“route”][0][“direction”][0][“direction_name”] trainLine = data2[“mode”][0][“route”][0][“route_name”] timeAwayRound = Utils.round timeAway/60, 0 stationText2.html = “The next “ + trainDir + “ “ + trainLine + “ train is “ + timeAwayRound + “ mins away.”
```

This grabs the “stop_id” (the nearest subway stop) from the first API, and plugs it into the request for the second API.

Then, we just have to wade through the data to extract what we need.

“timeAway” gives us how far the nearest train is away, in seconds.

“trainDir” gives us the direction the train is headed.

And “trainLine” tells us which service line the train is on.

Then we created a quick formula to turn seconds into minutes, and dumped all of that data into a string that made sense.

And voila! A little bit of quick UI, some fancy animation, and we had it!

![Image](https://cdn-media-1.freecodecamp.org/images/aJoSvFXbdykSsyTK8UKL88MuzJ42ros0MVhg)
_You can try out the prototype for yourself here: [http://share.framerjs.com/7ygqcpa64f67/](http://share.framerjs.com/7ygqcpa64f67/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/36y4vd20skFFxWO1tomXfMF50MS3pwNpffCv)
_“Like…Whoa…”_

### Takeaways

I learned so much in building this. Working with real data is so liberating once you figure it out.

I cannot over-emphasize: if you haven’t gotten practice with reading API documentation yet, it can be quite frustrating. Be patient. It may take several hours to figure these out and get them working.

The syntax has to be perfect. And I mean _perfect_.

But if you do get it, you’ll be standing there, playing with it and watching the numbers change with a smile on your face.

And you’ll feel like, all of a sudden…you know kung fu.

![Image](https://cdn-media-1.freecodecamp.org/images/J6Ptdawe8FTEBoH0nsRDtuKfyhjudqYWUyfY)

Thanks for reading. [Give the prototype a try](http://share.framerjs.com/7ygqcpa64f67/). I would love your feedback!

Also, be sure to check out [my first article](https://blog.prototypr.io/designing-with-framer-part-1-faking-it-vs-making-it-ce74e1ca980) about prototyping with FramerJS.

_If you liked this, click the? below so other people will see this here on Medium._

