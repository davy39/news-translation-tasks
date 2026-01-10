---
title: 'Searching for rivers in Unterfranken: how to use Elasticsearch to find features
  on a map'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T23:25:16.000Z'
originalURL: https://freecodecamp.org/news/searching-for-rivers-in-unterfranken-how-to-use-elasticsearch-to-find-features-on-a-map-756017ff28c7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H2M5xGnz5mqH_y760kT7-g.jpeg
tags: []
seo_title: null
seo_desc: 'By 24ma13wg

  One of the great things about working remotely is that I can work from wherever
  I want to. So, this month I have swapped my city desk in London for one in the spa
  town of Bad Kissingen, Germany.

  I’ve also had fun building search engines w...'
---

By 24ma13wg

One of the great things about working remotely is that I can work from wherever I want to. So, this month I have swapped my city desk in London for one in the spa town of Bad Kissingen, Germany.

I’ve also had fun building search engines with [Elasticsearch](https://www.elastic.co/). In this post, I’m going to explore how it can be used to search for features on a map.

### Search indices

Sitting here at my new desk, I’m leafing through an old textbook. At the back, there is an index. It tells me on which pages certain keywords appear. So, if I want to read about something specific I can find the relevant page numbers quickly. Without the index, I would have to scan through all the pages of the book to find what I’m interested in.

Similarly, when we search for things on the internet — although we may not be aware of it — we are, likely, also using a (more sophisticated) index to make our search fast. We put questions to the index and get answers back. More accurately, with regard to Elasticsearch, we query the index by sending RESTful API requests, in the form of [JSON](https://www.json.org/). Results are returned.

### The JSON family

JSON is a commonly used format for giving structure to data. Put simply, it expresses data as groups of name/value pairs, in a text string. For example:

```
{  "city": "Erlangen",  "country": "Germany"},{  "city": "Würzburg",  "country": "Germany"}
```

Minified, our example looks like this:

```
{"city":"Erlangen","country":"Germany"},{"city":"Würzburg","country":"Germany"}
```

Often we are concerned with indexing fields of data, like a product record, or full text, like a blog post. Elasticsearch handles these very well. It can also index spatial data: map features, such as locations and boundaries. We use a special kind of JSON to describe map features, called [GeoJSON](http://geojson.org/). It looks like this:

```
{  "type": "Feature",  "geometry": {    "type": "Point",    "coordinates": [49.792762, 9.939119]  },  "properties": {    "city": "Würzburg",    "country": "Germany"  }}
```

A geometry type may be a: `Point`, `LineString`, or `Polygon`. There are multi types for these: `MultiPoint`, `MultiLineString`, and `MultiPolygon`. Several features, like the above location, can be contained within a `FeatureCollection`.

Bad Kissingen is one of many communities in the Lower Franconia region (_Unterfranken_ in German). Like many of its neighbors, a river runs through it: the Fränkische Saale. The boundary of the community forms a single shape; it maps to the `Polygon` geometry type. The water courses that make up the river can be imagined as a series of lines joined together. They map to the `MultiLineString` type.

I’ve found some maps of Lower Franconia online. I can process all the region’s rivers and communities into [NDJSON](http://ndjson.org/) (newline delimited — another variation of JSON). I create an Elasticsearch index, and load the data into it. Now I’m ready to search. _Gut, wir machen einen Test!_

### Searching for rivers

A simple term query tells me that there are 22 rivers and 360 communities in Lower Franconia. There are many more water courses in the downloaded data, but only 22 are defined as rivers. Time to try some more complex queries. I’ll begin with the region’s principal river, the river Main, which sounds like _Mine_ in German. I wonder how many communities it flows through? The query I send to my index looks like this:

```
GET lower_franconia/default/_search{  "query": {    "bool": {      "filter": [        {          "term": {            "feature": "community"          }        },         {          "geo_shape": {            "geometry": {              "indexed_shape": {                "index": "lower_franconia",                "type": "default",                "id": "12",                "path": "geometry"              },              "relation": "intersects"            }          }        }      ]    }  }}
```

This query is being run in a `filter` context. This means that relevance scores are not calculated. I'm not concerned with how well things match, but rather whether a match exists or does not. In this context, I specify an array of two items.

In the first item, I am specifying a `term` key with community features as a constraint. This means that only documents in my index which have a value of `community` in the `feature` field will be returned.

In the second item of the array, I have a `geo_shape` query specifying document number `12` (this document describes the river Main) and a relationship of `intersects` as the constraints.

Put simply, match all community shapes that intersect with a particular river line.

I get 91 hits. A quarter of all communities are on the Main. The result is formatted in — yes you guessed it — JSON. Although JSON is quite readable, it’s not easy to understand at a glance. Better to create a data visualization with [d3.js](https://d3js.org/) so that the results can be understood instantly.

![Image](https://cdn-media-1.freecodecamp.org/images/fO0y5H9ExU-h5xOB5lPQFK3GcVKhEn2OdHCJ)
_Hey Elasticsearch, which communities does the river Main flow through?_

For more details about how this is done, see my previous post on web page cartography.

[**Could a brown bear, a black bear, and a polar bear meet?**](https://towardsdatascience.com/could-a-brown-bear-a-black-bear-and-a-polar-bear-meet-9b82f4a9948d)  
[_Web page cartography can show us where_towardsdatascience.com](https://towardsdatascience.com/could-a-brown-bear-a-black-bear-and-a-polar-bear-meet-9b82f4a9948d)

Next up, how many rivers are close by? If I want to stroll by a river this evening, but don’t want to travel, say more than ten kilometers, what are my options?

![Image](https://cdn-media-1.freecodecamp.org/images/-Slqcj8PvbRjm1UJLTAEwli3-xnpz24uUbNZ)
_How many rivers are within ten kilometers of my desk?_

Four hits come back: the rivers Aschach, Fränkische Saale, of course, Thulba, and Premich. This query is slightly different from the previous one. This time I only want rivers to be returned. Also, I am specifying a new shape that does not exist in the index. A circle which is centered on my current location with a radius of ten kilometers.

One more. Where shouldn’t I go if I want to walk by a river? For this query, I use a `must_not` key to filter out the communities that intersect with any of the 22 rivers. I get 199 hits – just over half of the communities in Lower Franconia are without a river.

![Image](https://cdn-media-1.freecodecamp.org/images/3gwAiE6woLLZ88N9f8-Ln3IALfcyMCScjWFQ)
_Which communities do not have a river?_

### Real world application

I have used the rivers and communities of Lower Franconia as a simple example to illustrate how map features can be indexed with Elasticsearch, and the query results visualized with d3.js.

Could it have a practical application? Well, the index could be used, for example, to find out which communities to warn if a flood alert was issued for a particular river. Perhaps it could be used, in a drier region, to predict where droughts might cause problems for agriculture.

Of course, we are not limited to river courses and community boundaries. Any combination of map features can be mapped and indexed and, therefore, there are many possible applications.

_Data: [OpenStreetMap](https://www.geofabrik.de) + [Open Data Portal des Freistaats Bayern](https://opendata.bayern.de)_

_Originally published at [24ma13wg.github.io](https://24ma13wg.github.io/searching-for-rivers-in-unterfranken/page.html)._

