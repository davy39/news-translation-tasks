---
title: How to scrape with Ruby and Nokogiri and map the data
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T22:52:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-with-ruby-and-nokogiri-and-map-the-data-bd9febb5e18a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kUyC5E-rXXkL4DcR8L91rA.jpeg
tags:
- name: Nokogiri
  slug: nokogiri
- name: google maps
  slug: google-maps
- name: JavaScript
  slug: javascript
- name: Ruby
  slug: ruby
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrew Bales

  Sometimes you want to grab data from a website for your own project. So what do
  you use? Ruby, Nokogiri, and JSON to the rescue!

  Recently, I was working on a project to map data about bridges. Using Nokogiri,
  I was able to capture a c...'
---

By Andrew Bales

Sometimes you want to grab data from a website for your own project. So what do you use? Ruby, Nokogiri, and JSON to the rescue!

Recently, I was working on a project to map [data about bridges](https://bridgereports.com/). Using Nokogiri, I was able to capture a city’s bridge data from a table. I then used links within that same table to scrape associated pages. Finally, I converted the scraped data to JSON and used it to populate a Google Map.

This article walks you through the tools I used and how the code works!

See the full code on my [GitHub](https://github.com/agbales/wichita-bridges) repo.

Live map demo [here](https://agbales.github.io/wichita-bridges/).

### The Project

My goal was to take a table from a bridge data [website](https://bridgereports.com/) and turn it into a Google map with geolocated pins that would produce informational popups for each bridge.

![Image](https://cdn-media-1.freecodecamp.org/images/pTodl03NV9GsnFl6mYtcO0-rPk6F8AUjRyBb)
_The Idea: HTML Table to Map_

To make this happen, I’d need to:

1. Scrape data from the original website.
2. Convert that data into a [JSON object](https://www.w3schools.com/js/js_json_objects.asp).
3. Apply that data to make a new, interactive map.

Your project will vary, surely — how many people are trying to map antique bridges? — but I hope this process will prove useful for your context.

### Nokogiri

Ruby has an amazing web scraping gem called [Nokogiri](https://github.com/sparklemotion/nokogiri). Among other features, it allows you to search HTML documents by CSS selectors. That means if we know the ids, classes, or even types of elements where the data is stored in the DOM, we’re able to pluck it out.

#### The scraper

If you’re following along with the [GibHub repo](https://github.com/agbales/wichita-bridges), you can find my scraper in bridges_scraper.rb

```
require 'open-uri'require 'nokogiri'require 'json'
```

Open-uri lets us open the HTML like a file and pass it to Nokogiri for the heavy lifting.

In the code below, I’m passing the DOM information from the URL with the bridge data over to Nokogiri. I then find the table element holding the data, search for its rows, and iterate through them.

```
url = 'https://bridgereports.com/city/wichita-kansas/'html = open(url)
```

```
doc = Nokogiri::HTML(html)bridges = []table = doc.at('table')
```

```
table.search('tr').each do |tr|  bridges.push(    carries: cells[1].text,    crosses: cells[2].text,    location: cells[3].text,    design: cells[4].text,    status: cells[5].text,    year_build: cells[6].text.to_i,    year_recon: cells[7].text,    span_length: cells[8].text.to_f,    total_length: cells[9].text.to_f,    condition: cells[10].text,    suff_rating: cells[11].text.to_f,    id: cells[12].text.to_i  )end
```

```
json = JSON.pretty_generate(bridges)File.open("data.json", 'w') { |file| file.write(json) }
```

Nokogiri has lots of methods (here’s a [cheat sheet](https://github.com/sparklemotion/nokogiri/wiki/Cheat-sheet) and a starter [guide](https://readysteadycode.com/howto-parse-html-with-ruby-and-nokogiri)!). We’re using just a few.

The table is found with **.at(‘table’)**, which returns the first occurrence of a table element in the DOM. This works just fine for this relatively simple page.

With the table in hand, **.search(‘tr’)** provides an array of the row elements that we iterate over with **.each**. In each row, the data is cleaned up and pushed into a single entry for the bridges array.

After all the rows are collected, the data is converted into JSON and saved in a new file called “data.json”.

### Combining data from multiple pages

In this case, I needed information from other associated pages. Specifically, I needed the latitude and longitude of each bridge, which was not featured on the table. However, I found that the link in the first cell of each row led to a page that _did_ provide those details.

I needed to write code that did a few things:

* Gathered links from the first cell in the table.
* Created a new Nokogiri object from the HTML on that page.
* Pluck out the latitude and longitude.
* Sleep the program until that process completes.

```
cells = tr.search('th, td')  links = {}  cells[0].css('a').each do |a|    links[a.text] = a['href']  end    got_coords = false    if links['NBI report']    nbi = links['NBI report']    report = "https://bridgereports.com" + nbi    report_html = open(report)    sleep 1 until report_html    r = Nokogiri::HTML(report_html)        lat = r.css('span.latitude').text.strip.to_f    long = r.css('span.longitude').text.strip.to_f
```

```
    got_coords = true  else    got_coords = true  end    sleep 1 until got_coords == true
```

```
  bridges.push(        links: links,        latitude: lat,        longitude: long,        carries: cells[1].text,        ..., # all other previous key/value pairs  )end
```

A few additional things are worth pointing out here:

* I’m using the “got_coords” as a simple binary. This is set to **false** by default and is toggled when the data is captured OR simply not available.
* The latitude and longitude are located in spans with corresponding classes. That makes securing the data simple: **.css(‘span.latitude’)** This is followed by **.text, .strip** and **.to_f** which 1) gets the text from the span, 2) strips any excess whitespace, and 3) converts the string to a float number.

### **JSON → Google Map**

The newly formed JSON object has to be modified a touch to fit the Google Maps API. I did this with JavaScript inside **map.js**

The JSON data is accessible within **map.js** because it has been moved to the JS folder, assigned to a variable called “bridge_data”, and included in a <script> tag in index.html.

All right! We’ll now convert the JSON file (assigned to the variable bridge_data) to a new array that’s usable by Google Maps.

```
const locations = bridge_data.map(function(b) {  var mapEntry = [];  var info = "<b>Built In: </b>" + b.year_build + "<br>" +             "<b>Span Length: </b>" + b.span_length + " ft<br>" +             "<b>Total Length: </b>" + b.total_length + " ft<br>" +             "<b>Condition: </b>" + b.condition + "<br>" +             "<b>Design: </b>" + b.design + "<br>";  mapEntry.push(    info,    b.latitude,    b.longitude,    b.id  )  return mapEntry;});
```

I’m using [.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) to create a new dimensional array called “locations”. Each entry has info, which will appear in our Google Maps popup if the user clicks on that pin on the map. We also include the latitude, longitude, and unique bridge ID.

![Image](https://cdn-media-1.freecodecamp.org/images/gjvu5vBL3amtEBBZrFs1z33vm2ZQdbq0khIM)
_Bridge map from JSON data_

The result is a Google Map that plots the array of locations with info-rich popups for each bridge!

Did this help you? Give it a few claps and follow!

