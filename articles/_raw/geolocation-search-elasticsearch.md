---
title: How to Set Up Geolocation Search in Your App with Elasticsearch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-07T17:12:37.000Z'
originalURL: https://freecodecamp.org/news/geolocation-search-elasticsearch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd644e7e6787e098393e278.jpg
tags:
- name: database
  slug: database
- name: elasticsearch
  slug: elasticsearch
- name: geolocation
  slug: geolocation
- name: search
  slug: search
seo_title: null
seo_desc: 'By Pramono Winata

  Location-based features are pretty common in apps nowadays. These features might
  seem complicated, but they can actually be implemented quite easily with Elasticsearch.

  Elasticsearch is a NoSQL database with a document-based structu...'
---

By Pramono Winata

Location-based features are pretty common in apps nowadays. These features might seem complicated, but they can actually be implemented quite easily with Elasticsearch.

Elasticsearch is a NoSQL database with a document-based structure. It's often used as a Search Engine. It also provides its own syntax and many tools to help your search be as flexible as possible.

In this article I will show you a simple way to search by geolocation by getting a list of cities by coordinate range.

## How to Install Elasticsearch

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1-4thJErMA9UpuP1jEBLRWFQ.png)

You can find an easy-to-follow [installation guide](https://www.elastic.co/guide/en/elasticsearch/reference/7.4/install-elasticsearch.html) on Elasticsearch's website. At the time I am writing this article, I am using Elasticsearch version 7.4.2 .

Just keep in mind that Elasticsearch has made a lot of changes in recent versions, one of them being the [removal of mapping types.](https://www.elastic.co/guide/en/elasticsearch/reference/master/removal-of-types.html) So if you are using another version of Elasticsearch some things here might not fully work.

After finishing your installation, do not forget to run your Elasticsearch service, which they emphasize clearly in their installation guide (for Linux, do this `./bin/elasticsearch` ).

**Make sure your elasticsearch is running** by using a GET request into port 9200 in your local machine, like this: [`GET http://localhost:9200`](http://localhost:9200)

## How to Make Your Elasticsearch Index

An index is similar to table in a regular database. For this example, let's make an index named `cities` that will contain our data.

Let's also define a simple model for our data: 

* `id` : `keyword` for our identifier
* `name` : `text` for the city name
* `coordinate` : `geo_point` to store our city coordinates (neat, they have this data-type already)

In Elasticsearch, we create the index by making a curl into an API. In our case our request will be like this:

```
PUT http://localhost:9200/cities
```

```json
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "id": {
                "type": "keyword"
            },
            "name": {
                "type": "text"
            },
            "coordinate": {
                "type": "geo_point"
            }
        }
    }
}
```

When you used that curl, you should get a response like this to verify that your index has been created:

```json
{
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "cities"
}

```

Nicely done! Now your index is ready to be used. Let's go ahead and play around with our newly created index.

## How to Populate Elasticsearch Data

We will now fill our Elasticsearch index with documents. If you are not familiar with this term, just know that it is very similar to rows in a SQL database.

In Elasticsearch, it's possible to store data that doesn't match with our predefined schema. But we will not do that here – instead we will insert data that matches our predefined schema.

Since we will be inserting multiple data at once, we will use the [bulk](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) API that Elasticsearch provides that allows multiple insertions in one API call.

In the example below, I will be inserting 9 cities into my index. Feel free to add more if you wish.

`POST '[http://localhost:9200/cities/_bu](http://localhost:9200/cities/_bu)lk`

```json
{ "index":{"_index": "cities" } }
{ "id": 1, "name": "Jakarta", "coordinate": {  "lat": -6.2008, "lon": 106.8456}}
{ "index":{"_index": "cities" } }
{ "id": 2, "name": "Tokyo", "coordinate": {  "lat": 35.6762, "lon": 139.6503} }
{ "index":{"_index": "cities" } }
{ "id": 3, "name": "Hong Kong", "coordinate": {  "lat": 22.3193, "lon": 114.1694} }
{ "index":{"_index": "cities" } }
{ "id": 4, "name": "New York", "coordinate": {  "lat": 40.7128, "lon": -74.0060} }
{ "index":{"_index": "cities" } }
{ "id": 5, "name": "Paris", "coordinate": {  "lat": 48.8566, "lon": 2.3522} }
{ "index":{"_index": "cities" } }
{ "id": 6, "name": "Bali", "coordinate": {  "lat": -8.3405, "lon": 115.0920} }
{ "index":{"_index": "cities" } }
{ "id": 7, "name": "Berlin", "coordinate": {  "lat": 52.5200, "lon": 13.4050} }
{ "index":{"_index": "cities" } }
{ "id": 8, "name": "San Fransisco", "coordinate": {  "lat": 37.7749, "lon": -122.4194} }
{ "index":{"_index": "cities" } }
{ "id": 9, "name": "Beijing", "coordinate": {  "lat": 39.9042, "lon": 166.4074} }

```

The payload might looks weird since it's in an incorrect JSON format, but don't worry – it's supposedly designed that way.

It should then reply back to you with a response similar to this:

```
{
    "took": 72,
    "errors": false,
    "items": [
        //will contains item for each data inserted
        ...
    ]
}
```

## How to Query Your Elasticsearch Documents

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-276.png)
_Photo by [Unsplash](https://unsplash.com/@chrislawton?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Chris Lawton</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Now comes the interesting part. We are going to do some querying with the documents that we inserted before.

Elasticsearch supports many types of syntax for query searching. It also has geolocation type searching which we will play around with today.

We can simply start searching for our cities with curl like this:

`POST '[http://localhost:9200/cities/_sear](http://localhost:9200/cities/_sear)ch`

```json
{
  "query": {
    "bool": {
      "filter": {
        "geo_distance": {
          "distance": "10km",
          "coordinate": {
            "lat": 37.76,
            "lon": -122.42
          }
        }
      }
    }
  }
}
```

That query should give me San Francisco, and the coordinates 37.7749 and -122.4194 should be inside a 10km distance radius from our coordinates (courtesy of Google).

```
{
    "took": 7,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 1,
            "relation": "eq"
        },
        "max_score": 0.0,
        "hits": [
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "eKPspHYBivyIhfWHb2vl",
                "_score": 0.0,
                "_source": {
                    "id": 8,
                    "name": "San Fransisco",
                    "coordinate": {
                        "lat": 37.7749,
                        "lon": -122.4194
                    }
                }
            }
        ]
    }
}
```

Congratulations! Now you have your own location search engine.   
But let's experiment a bit more. Let's say you want to get more cities in that location.

Let's try to expand the distance to 4500km by changing the payload:

```json
{
  "query": {
    "bool": {
      "filter": {
        "geo_distance": {
          "distance": "4500km",
          "coordinate": {
            "lat": 37.76,
            "lon": -122.42
          }
        }
      }
    }
  }
}
```

And you should get this response:

```
{
    "took": 8,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 0.0,
        "hits": [
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "dKPspHYBivyIhfWHb2vl",
                "_score": 0.0,
                "_source": {
                    "id": 4,
                    "name": "New York",
                    "coordinate": {
                        "lat": 40.7128,
                        "lon": -74.0060
                    }
                }
            },
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "eKPspHYBivyIhfWHb2vl",
                "_score": 0.0,
                "_source": {
                    "id": 8,
                    "name": "San Fransisco",
                    "coordinate": {
                        "lat": 37.7749,
                        "lon": -122.4194
                    }
                }
            }
        ]
    }
}
```

It gives two results: New York and San Fransisco. The results look correct, but the positioning might be a bit weird. San Fransisco supposedly should come first since it's closer, right?

Well not exactly, since what we are doing is just filtering. Our query is just filtering and it doesn't care about which one is closest to you. 

But what if we want to do some calculation to show which locations might be the nearest? Don't worry, Elasticsearch can do that too. We can use a type of query called a function score query.

### How to Use a Function Score Query in Elasticsearch

Elasticsearch calculates (scores) what documents it will show to the user. By using [function score queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html) we can modify that score so we can determine which documents should be returned.

Here, we will be using the [decay query function](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html#function-decay). There are three kinds of decay functions: exp, linear, and gauss. Each of them has different behaviors.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/decay_2d.png)
_Image [source](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html#function-decay)_

The one we will use here is the linear type function. We will also specify the coordinates together with offset and scale.

`POST '[http://localhost:9200/cities/_sear](http://localhost:9200/cities/_sear)ch`

```
{
  "query": {
    "function_score": {
      "functions": [
        {
          "linear": {
            "coordinate": {
              "origin": "37, -122",
              "offset": "100km",
              "scale":"2500km"
            }
          }
        }
      ],
       "min_score":"0.1"
    }
  }
}
```

Now, we should get our results ordered by the highest score.

```
{
    "took": 32,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 1.0,
        "hits": [
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "eKPspHYBivyIhfWHb2vl",
                "_score": 1.0,
                "_source": {
                    "id": 8,
                    "name": "San Fransisco",
                    "coordinate": {
                        "lat": 37.7749,
                        "lon": -122.4194
                    }
                }
            },
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "dKPspHYBivyIhfWHb2vl",
                "_score": 0.19508117,
                "_source": {
                    "id": 4,
                    "name": "New York",
                    "coordinate": {
                        "lat": 40.7128,
                        "lon": -74.0060
                    }
                }
            }
        ]
    }
}
```

And that wraps it up!

## Conclusion

In this article, we've covered how to implement location-based search with Elasticsearch. But this is not the end – what I have shown here is just the surface of what you can do. 

I hope you found this article interesting and useful. If so, keep learning more about it and try to experiment with combining function scoring. It will be fun, I promise.

> Always be curios and you will learn something new.

