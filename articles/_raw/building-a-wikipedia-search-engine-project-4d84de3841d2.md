---
title: Building a Wikipedia Search App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-12T15:43:31.000Z'
originalURL: https://freecodecamp.org/news/building-a-wikipedia-search-engine-project-4d84de3841d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t0FLqKuduU0MH0tT6mvG9w.jpeg
tags:
- name: api
  slug: api
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: learning
  slug: learning
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Ayo Isaiah

  I just finished Free Code Camp’s Wikipedia Viewer app, where you pull articles side-by-side
  from Wikipedia using the MediaWiki Web API.

  The agile user stories were:


  Users can type queries in a search box and view the resulting Wikipedi...'
---

By Ayo Isaiah

I just finished Free Code Camp’s [Wikipedia Viewer](https://www.freecodecamp.com/challenges/build-a-wikipedia-viewer) app, where you pull articles side-by-side from Wikipedia using the MediaWiki Web API.

The agile user stories were:

* Users can type queries in a search box and view the resulting Wikipedia entries.
* Users can view random Wikipedia articles by clicking a button.

I finished this project rather quickly, because I knew exactly what to do after looking at the MediaWiki API, which was perhaps thanks to my experience from the [Weather Project](http://www.ayoisaiah.com/weather-app/).

#### Design

![Image](https://cdn-media-1.freecodecamp.org/images/TC-gTYPg3lFv5q4LkFi5hnNb0y9OdMgEaTd1)

While thinking up design ideas for this project, I decided to lookup Google’s homepage and its search results page to see how they handled things. I ended up taking most of my design inspiration from them, as you’ll see.

First up, the homepage has the headline, search box and buttons at the centre of the page. The “I’m Feeling Lucky” button sends you to a random Wikipedia Page which fulfilled the second user story.

When the page loads, focus is given to the search box so that the user can begin typing their query immediately, thanks to the following JavaScript:

```
window.onload = function() { document.getElementById("wiki-search-input").focus();};
```

One thing I experimented with a bit is getting the results page to show up as soon as you start typing in the search box, imitating this feature on Google search.

![Image](https://cdn-media-1.freecodecamp.org/images/bul6ePnr10cm5B4Bd8Phw-n92T3doIbodTTr)

I was able to replicate this on my app, but I wasn’t sure how it was going to function on touch screens because, in my tests, the page didn’t respond to keypresses on my phone.

So to avoid unexpected behavior, I ditched this idea and showed the results page only when the query was fully entered, and the “search” button or enter key was pressed. This worked fine across all the mobile and desktop platforms I tested.

Overall, my design is nothing revolutionary, but so long as it scales properly on all device types, it’s good enough for me.

#### Logic

Diving into the code that pulled the results from Wikipedia, it wasn’t all that hard to use the API to be honest.

I tried to tackle this challenge using the jQuery _$.getJSON_ method to make the API call as I did with the Open Weather API, but it returned an error message concerning Cross Origin Resource Sharing (CORS).

On further investigation, I found another jQuery method _$.ajax()_ on Stack Overflow which worked. Apparently, I had to specify the dataType as “JSONP” (JSON with Padding) to get it to work.

```
function ajax (keyword) {  $.ajax({     url: "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + keyword + "&prop=info&inprop=url&utf8=&format=json",    dataType: "jsonp",   success: function(response) {       console.log(response.query);       if (response.query.searchinfo.totalhits === 0) {         showError(keyword);       }
```

```
       else {         showResults(response);       }  },
```

```
   error: function () {    alert("Error retrieving search results, please refresh the page");   }  });
```

```
}
```

I discovered that the URL and title of each page were almost exactly the same. The only difference was that spaces in the title were replaced by underscores in the url.

So “JavaScript Libraries” becomes “JavaScript_Libraries” in the url.

Simply by grabbing each title, I replaced the spaces with underscores using a bit of Regex (which admittedly I don’t know very well yet) and affixed it to the corresponding search result.

```
var title = callback.query.search[m].title;var url = title.replace(/ /g, "_");
```

```
$(".title-" + m).html("<a href=’https://en.wikipedia.org/wiki/" + url + "' target='_blank'>" + callback.query.search[m].title + "</a>");
```

The last thing I did was to make an error function so that if a user’s query does not match any results, it will simply display a few tips on the page to help the user improve search.

![Image](https://cdn-media-1.freecodecamp.org/images/nxBqsMnB8FPT8Y-Wxw8XjAQAeWW-NcW1AtQn)

As you can see, Free Code Camp’s open source community doesn’t have a Wikipedia article yet (despite having more than 300,000 members). If you’re a frequent Wikipedia contributor, here’s [the outstanding article request](https://en.wikipedia.org/wiki/Wikipedia_talk:WikiProject_Education#Open_source_community_focused_on_coding_education_wants_your_help) for you to create one.

So that was pretty much it for this project. You can view the final result on [Codepen](http://codepen.io/ayoisaiah/full/Kzvrbp).

#### What’s next

I’m halfway done with the Twitch API Project as I write this. Most of the design is done, only need to figure out a few things with the API.

As a new semester at my University kicks off this week, things may become a bit slower with Free Code Camp, but nonetheless it shouldn’t stop me from putting a few hours in everyday.

If you want to reach out or connect with me, you can find me on [Twitter](https://twitter.com/ayisaiah) or [email me](mailto:ayisaiah@gmail.com).

Thanks for reading.

A version of this post was originally published on [my personal blog](http://ayoisaiah.com).

