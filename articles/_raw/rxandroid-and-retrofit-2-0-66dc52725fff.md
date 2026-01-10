---
title: RxAndroid and Retrofit 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-09-17T01:20:38.000Z'
originalURL: https://freecodecamp.org/news/rxandroid-and-retrofit-2-0-66dc52725fff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OlU3vLjcEhu-oKeGeAdqyA.png
tags:
- name: android app development
  slug: android-app-development
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: Retrofit
  slug: retrofit
- name: rxjava
  slug: rxjava
seo_title: null
seo_desc: 'By Ahmed Rizwan

  Ok, so this isn’t new or anything, but I thought let’s just make a simple tutorial
  with the new Retrofit 2.0. This should give us a starting point.

  This isn’t a tutorial for RxAndroid. If you don’t know much about RxAndroid, you
  shoul...'
---

By Ahmed Rizwan

Ok, so this isn’t new or anything, but I thought let’s just make a simple tutorial with the new Retrofit 2.0. This should give us a starting point.

This isn’t a tutorial for RxAndroid. If you don’t know much about RxAndroid, you should first check [this](https://medium.com/@ahmedrizwan/rxandroid-and-kotlin-part-1-f0382dc26ed8) out.

Let’s get into it then. Here are the things you’ll need before we start:

1. [RxAndroid](https://github.com/ReactiveX/RxAndroid) and [Retrofit](https://github.com/square/retrofit)
2. [Gson](https://github.com/google/gson) (I’ll be using Gson, you can use other parsers as well)
3. An Internet connection!

So after you’ve added the dependencies, your gradle files should look something like this (ignore the [Retrolambda](https://github.com/evant/gradle-retrolambda) plugin, I just added it for code conciseness because… Lambdas! *_*):

Now you might be wondering, what is Retrofit exactly? Well, Retrofit is an HTTP Client, but it’s type-safe. That means you can transform an HTTP API into a Java Interface. This makes it ridiculously convenient to interact with the API.

### The Starting Example

In the example, I’m going to use the [OpenWeather API](http://openweathermap.org) and I’ll keep it as simple as possible. I’ll just get the [weather forecast for today](http://openweathermap.org/current) in three steps.

#### Step 1: Generate Java Model (Pojo) classes from JSON

Here’s the API URL:

```
http://api.openweathermap.org/data/2.5/weather?q=London
```

And the response returned when you call it is:

```
{ “coord”: { “lon”: -0.13, “lat”: 51.51 }, “weather”: [ { “id”: 521, “main”: “Rain”, “description”: “shower rain”, “icon”: “09d” } ], “base”: “cmc stations”, “main”: { “temp”: 289.49, “pressure”: 993, “humidity”: 67, “temp_min”: 285.93, “temp_max”: 291.15 }, “wind”: { “speed”: 8.7, “deg”: 210, “gust”: 14.4 }, “rain”: { “1h”: 1.02 }, “clouds”: { “all”: 40 }, “dt”: 1442242382, “sys”: { “type”: 1, “id”: 5091, “message”: 0.0052, “country”: “GB”, “sunrise”: 1442208848, “sunset”: 1442254609 }, “id”: 2643743, “name”: “London”, “cod”: 200}
```

Looks pretty messy, right? Well, don’t worry, just go to this awesome [website](http://www.jsonschema2pojo.org) and paste in the JSON. It’ll come out looking like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pD1QD3UiI0A4M9yidSIaVQ.png)

If the JSON has to many model classes to be generated, the easier thing to do is generate a **Jar** and download it, extract it, and then add the files. Otherwise just click on Preview, and copy-paste the classes you need. Do remove the **@Generated(“org.jsonschema2pojo”)** from each model class, as this annotation isn’t recognized by Android by default.

I downloaded the Jar because there are a lot of classes. And also because I’m lazy. :)

After extracting and adding the classes, now the project tree looks something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HCtSwhgbB3ERajLMixmuyQ.png)

So far, so good!

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Aok7yzCTbxShebikqfTsw.png)
_Just an evil raccoon being evil._

#### Step 2: Create Retrofit Interface for your API calls

For Retrofit, you have to create an interface for the endpoints of your API.

When creating the interface, you should ask yourself: what exactly is the meaning of life? And secondly: what information do I need from the API?

For me, the answer to both questions is WeatherData (the top-most object). Now let’s examine the URL:

```
http://api.openweathermap.org/data/2.5/weather?q=London
```

There’s a **query** at the very end, so I’ll do this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*MDro75UsBFVQHUVFVgAtEg.png)

```
Note: in Retrofit 2.0, the endpoint path string should NOT start with “/” 
```

```
@GET("/weather?") --> incorrect@GET("weather?")  --> correct
```

Now as parameter, I’ll send the query value using the @Query annotation.

As you’ll notice, I’m returning the **Observable** of WeatherData. That’s Rx right there!

#### Step 3: Create the Retrofit Adapter and WeatherService instance

Now in our Activity, we have to create a Retrofit adapter using the Base URL, along with some other info. Once built, we can initiate an object of **WeatherService** interface, then call the method.

Take a look at this delicious code:

So the question here is what the hell are those _addCallAdapter_ and _addConverterFactory_ methods doing there?

Well in order for our calls to return type **Observable**, we have to set the call adapter to **RxJavaCallAdapter**.

And addConverFactory is there to tell Retrofit which sort of converter I want it to use for serializing the JSON. I prefer the GSON converter. There are other converters available too.

So, for these two you need to add their dependencies to your gradle:

```
compile 'com.squareup.retrofit2:adapter-rxjava:2.0.2'compile 'com.squareup.retrofit2:converter-gson:2.0.0'
```

Now run the code, and voila! It’ll log the weather description.

### A Different Example

So yeah… Another example! Because why not? This time, I’ll try out the GitHub API. Again just 3 steps.

First, the API call URL:

```
https://api.github.com/users/ahmedrizwan
```

and the response:

```
{    "login": "ahmedrizwan",    "id": 4357275,    "avatar_url": "https://avatars.githubusercontent.com/u/4357275?v=3",    "gravatar_id": "",    "url": "https://api.github.com/users/ahmedrizwan",    "html_url": "https://github.com/ahmedrizwan",    "followers_url": "https://api.github.com/users/ahmedrizwan/followers",    "following_url": "https://api.github.com/users/ahmedrizwan/following{/other_user}",    "gists_url": "https://api.github.com/users/ahmedrizwan/gists{/gist_id}",    "starred_url": "https://api.github.com/users/ahmedrizwan/starred{/owner}{/repo}",    "subscriptions_url": "https://api.github.com/users/ahmedrizwan/subscriptions",    "organizations_url": "https://api.github.com/users/ahmedrizwan/orgs",    "repos_url": "https://api.github.com/users/ahmedrizwan/repos",    "events_url": "https://api.github.com/users/ahmedrizwan/events{/privacy}",    "received_events_url": "https://api.github.com/users/ahmedrizwan/received_events",    "type": "User",    "site_admin": false,    "name": "ahmed",    "company": null,    "blog": "https://medium.com/@ahmedrizwan",    "location": null,    "email": "ahmedrizwan@outlook.com",    "hireable": true,    "bio": null,    "public_repos": 19,    "public_gists": 0,    "followers": 25,    "following": 16,    "created_at": "2013-05-06T18:32:59Z",    "updated_at": "2016-07-08T11:29:26Z"}
```

Again, the JSON looks pretty messy.

#### **Step 1: Generate the Pojos (plain old Java objects)**

I copied the response and pasted it [here](http://www.jsonschema2pojo.org) (yet again):

![Image](https://cdn-media-1.freecodecamp.org/images/1*gHJzvU0FcKSNWe6yTjSvLg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*67owad0Zun8o84QOrAWaUA.png)

And clicked on Preview.

Then I copied the Github class into my Project. *music intensifies*

#### **Step 2: Create Interface for Endpoints**

Now examine the API URL. And I mean, really examine it. You’ll see the endpoint starts from users and ends with the username.

```
https://api.github.com/users/ahmedrizwan
```

So the interface I created looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*jabUA4iGndv51G0d7Pi_9A.png)

I created a call method, and used **@Path** annotation to replace the value of _{username}_ in the EndPoint string dynamically.

#### **Step 3: Create adapter and instance of GithubService**

Here’s the beautiful code for doing just that:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gEbFR7b6wmJWNJg1sSe9sA.png)

You’ll notice I’m mapping the user object to String (you can do that with Rx. So Its output becomes:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hoXm3j3xqKF9HbEBWK73kQ.png)

So this is it. Although the article doesn’t cover everything Retrofit and RxAndroid can do (of course), I hope it will get you off to a good start.

Happy coding!

