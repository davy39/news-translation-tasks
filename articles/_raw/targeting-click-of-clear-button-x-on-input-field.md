---
title: Targeting Click of “Clear” Button (X) on Input Field
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/targeting-click-of-clear-button-x-on-input-field
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a98740569d1a4ca2689.jpg
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'jQuery makes it easy to get your project up and running. Though it''s fallen
  out of favor in recent years, it''s still worth learning the basics, especially
  if you want quick access to its powerful methods.

  But while jQuery is a powerful library, it ca...'
---

jQuery makes it easy to get your project up and running. Though it's fallen out of favor in recent years, it's still worth learning the basics, especially if you want quick access to its powerful methods.

But while jQuery is a powerful library, it can't do everything. That's where having solid understanding of vanilla JavaScript comes in handy.

Say you have a [Wikipedia Viewer](https://www.freecodecamp.org/learn/coding-interview-prep/take-home-projects/build-a-wikipedia-viewer) project like this:

```html
<div class="search">
  <p id="text">Search on Wikipedia</p>
  <input id="searchbox" type="search"></input>
  <button id="searchbutton">Search</button>
  <a href="https://en.wikipedia.org/wiki/Special:Random" target="_blank"><button id="searchbutton">Random Article</button></a>
  <div class="resultingarticles"></div>
</div>
```

```js
$("#searchbox").keyup(function(event) {
  if(event.keyCode === 13) {
    $("#searchbutton").click();
  };
});

$("#searchbutton").click(function() {
  
  var searchInput = document.getElementById("searchbox").value;
  searchInput = searchInput.toLowerCase();
  
  if(searchInput !== "") {
  
    var myRequest = new XMLHttpRequest();
    myRequest.open('GET','https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch='+ searchInput + '&utf8=&format=json&origin=*');
  
      myRequest.onload = function() {
      var searchResults = JSON.parse(myRequest.responseText);
      
      $(".resultingarticles").empty();  
        
      for(i=0; i<10; i++) {
        var articleTitle = searchResults.query.search[i].title;
        var articleSnippet = searchResults.query.search[i].snippet;
        var articleId = searchResults.query.search[i].pageid;
        var articleLink = "https://en.wikipedia.org/?curid=" + articleId;
        $(".resultingarticles").append("<a href='" + articleLink + "' target='_blank'>" + "<div class='article'>" + "<p>"+articleTitle+"</p>" + "<p>" + articleSnippet + "</p>" + "</div>" + "</a>");
      };
        
      };
    
    myRequest.send();
    
  };
});
```

Everything is working as you expect – you can enter text into the search box, hit enter or the "Search" button, and see a list of Wikipedia articles.

Because you're using `type="search"` on your `input` element, the Chrome browser will automatically add an "X" to the end of the input if there's text and you hover over the input. Note that other browsers might handle `type="search"` differently.

When you click on the "X", the text disappears.

But say you already have a list of articles, and when you clear the text, you also want to clear the populated articles:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-13-19-24.gif)

It turns out that clicking the "X" in the search box fires a "search" event. jQuery doesn't support the "search" event, so you'll have to write an event listener in vanilla JavaScript:

```js
document.getElementById("searchbox").addEventListener("search", function(event) {
  $(".resultingarticles").empty();  
});
```

Now when a search event is fired, you can use jQuery to clear the `div` element with the articles:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-13-19-29.gif)

