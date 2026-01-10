---
title: What does API Stand For? A Definition of the Coding Acronym in Plain English.
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-14T18:03:00.000Z'
originalURL: https://freecodecamp.org/news/what-does-api-stand-for-a-definition-of-the-coding-acronym-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/api-image.jpeg
tags:
- name: api
  slug: api
seo_title: null
seo_desc: 'Nope, API doesn''t stand for Apple Pie Inside. API stands for Application
  Programming Interface. APIs allow two applications to interface (or interact) with
  each other.

  An API a set of programming instructions and functions used to access a website
  or...'
---

Nope, API doesn't stand for Apple Pie Inside. API stands for Application Programming Interface. APIs allow two applications to interface (or interact) with each other.

An API a set of programming instructions and functions used to access a website or web-based software application. An API allows other developers to use your application's data and functionality. It allows your product to interact with other products.

APIs were first used in software and hardware development in the 1980s. But now when people talk about APIs they are usually referring to web APIs, or more specifically RESTful APIs. It has become common practice to use RESTful APIs when developing web-based applications.

A web API is basically a program that you interact with completely through URLs. Normally when you send a request to a URL with your browser a server sends back a response that displays for you to look at. Things are different when you send a request to a URL of an API. The server sends back something that is meant to be useful only to computer. An API returns data that can be used in a different website or program.

## What are APIs used for?

APIs are not meant to be used by an end-user. They are used for software to interact with other software. For instance, a website can make a call to the Open Weather API to get weather information to display on the website.

APIs are also sometimes used internally within a single company. They can be used to create internal websites and systems that interact with each other easily.

## **How does an API work?**

An API generally gives others access to a large amount of organized data. The gatekeeper of that data gives a developer permission (in the form of an _API key_) to ask a server for information. If the request is successful, the server responds with a message, usually in JSON or XML format.

Usually there will be documentation for an API you want to use called an API specification. This explains the controls and how to use the API.

Here is an example of the API specification for the OpenWeather API that allows you to get the current weather at a specific location: [https://openweathermap.org/current](https://openweathermap.org/current) 

API specifications contain a list of URLs you can use to retrieve data. Using one of the URLs is called an _API request_ or _API call_. Often the specification will show _parameters_ and the _response_ for each URL that is part of the API.

### Parameters

Parameters are what you add to the end of a URL to specify what information you want the API to return. Parameters are basically variables you pass in to the API.

The URL to get weather information from the OpenWeather API is:  
`api.openweathermap.org/data/2.5/weather`. 

However, you need to add a city as a parameter to specify which location to return weather data for. Here is the URL with the city parameter:   
[`api.openweathermap.org/data/2.5/weather?q=London`](http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22)

Sometimes parameters are required to get a response. Sometimes parameters are optional. In the OpenWeather API, it is required to supply a location, but there are other ways of specifying the location besides the city name. All the ways are given in the API specification.

Parameters can also specify things like:

* How should the results be sorted?
* How many results should be returned?
* What format should the results be in?
* What date range do you want results for?

### The Response

When you send a request to an API, you will get back a response. You will either get back the data you requested or a reason why the request failed.

Below is an example of a the response you get when you send the following request: [`api.openweathermap.org/data/2.5/weather?q=London`](http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22). It is a JSON response.

```javascript
{
    "coord": {
        "lon": -0.13,
        "lat": 51.51
    },
    "weather": [
        {
            "id": 300,
            "main": "Drizzle",
            "description": "light intensity drizzle",
            "icon": "09d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 280.32,
        "pressure": 1012,
        "humidity": 81,
        "temp_min": 279.15,
        "temp_max": 281.15
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.1,
        "deg": 80
    },
    "clouds": {
    	"all": 90
    },
    "dt": 1485789600,
    "sys": {
        "type": 1,
        "id": 5091,
        "message": 0.0103,
        "country": "GB",
        "sunrise": 1485762037,
        "sunset": 1485794875
    },
    "id": 2643743,
    "name": "London",
    "cod": 200
    }
```

An API response may not be formatted like this example. All the text is often on a single line. Since it is mainly meant to be read by a computer and not a person, the formatting does not matter.

### **API keys**

If you try the above URL yourself, you won't get the response above. It will probably look more like:

```javascript
{
    "cod": 401,
    "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."
}
```

Most APIs require some sort of authentication before they will return data. This is usually in the form of an _API key_. These keys are kind of like a password. They are a long string of letters and numbers that you have to send with your API request so the server knows you are allowed to access the information. 

For the OpenWeather API, and with many other APIs, you can get an API key for free after creating an account. Many companies use API keys on free APIs to make sure people don't make to many requests in one day. It could really bog down a server if a single person made thousands of requests every minute.

Some APIs are public without an API key. Below is an API that allows you to find rhyming words. Click the link, then try changing the final word in the URL to search for different rhyming words.

[https://api.datamuse.com/words?rel_rhy=camp](https://api.datamuse.com/words?rel_rhy=camp)

## Want to learn more?

If you want to learn more about using APIs, check out the video below on the freeCodeCamp.org YouTube channel.

%[https://www.youtube.com/watch?v=BYsTrGH6B2s]




