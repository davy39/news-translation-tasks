---
title: Build a Best Sellers List with New York Times and Google Books API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T03:13:27.000Z'
originalURL: https://freecodecamp.org/news/build-a-best-sellers-list-with-new-york-times-google-books-api-46201c30aec7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bVvh3q1aNXWnfkjXNp_vwQ.png
tags:
- name: Digital Humanities
  slug: digital-humanities
- name: api
  slug: api
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrew Bales

  A single API may not always have all of the data you need. In this article, we’ll
  walk through the steps to combine two APIs by using unique identifiers from the
  New York Times API to grab book covers from the Google Books API.

  You ca...'
---

By Andrew Bales

A single API may not always have all of the data you need. In this article, we’ll walk through the steps to combine two APIs by using unique identifiers from the New York Times API to grab book covers from the Google Books API.

You can find the full project on [GitHub](https://github.com/agbales/best-sellers) and view a demo on [CodePen](https://codepen.io/agbales/full/LNWPYW/).

Here are the steps we’ll cover:

1. Fetch best selling books data from the New York Times API.
2. Append listings to the DOM.
3. Query the Google Books API with ISBN numbers to add cover images to the listings.

At the end of the tutorial, you’ll have a best sellers list! Here’s a peek:

![Image](https://cdn-media-1.freecodecamp.org/images/ckGF3oZ3cWjkItnuviz8K66gLSGPI3Va9xil)

### Wait, but why?

I first began working on this project a little over a year ago. I was learning about APIs and requesting keys to practice accessing and displaying data.

While exploring the _New York Times_ API, I found that it was possible to get a list of best selling books. For each book on the list, the API provides a current rank and number of weeks on the list. It also offers info like a synopsis and an Amazon link.

I was able to populate textual info, but the list lacked the natural visual component of book covers. At the time, I didn’t see a clear road forward, so I put the project on the shelf.

**This is an instance where having access to an API is helpful, but incomplete.**

This week, I returned with the goal of adding books covers. I found that Google Books API will return thumbnails for books when provided an ISBN, a unique identifying number. As luck would have it, the New York Times API provides that ISBN.

We’re in business!

### Getting Started

First, we want to generate a list of the top selling fiction books with a bit of info about each. It would be nice to display information about how long the book has been on the list. We also need to see the cover and provide a link for users to learn more about the book or buy a copy.

The New York Times API provides all of that information except for the book cover. Grab a free [NYT API key](https://developer.nytimes.com) to get started.

We’ll use the [Fetch API](https://developers.google.com/web/updates/2015/03/introduction-to-fetch) to get the best seller data for hardcover works of fiction:

```
fetch('https://api.nytimes.com/svc/books/v3/lists.json?list-name=hardcover-fiction&api-key=' + apiKey, {    method: 'get',  })  .then(response => { return response.json(); })  .then(json => { console.log(json); });
```

If you inspect the browser, you’ll see a JSON object logged in the console. If you haven’t used an API before, it will be helpful to spend a moment looking through this object. Burrowing into the data to access exactly what you’re looking for may take a while to get used to.

The response returns 15 objects within “results”. Each result is one book. For clarity, this example uses `.forEach()` to drill down into the API response `nytimesBestSellers` looping over each book.

```
nytimesBestSellers.results.forEach(function(book) {  var isbn = book.isbns[1].isbn10;  var bookInfo = book.book_details[0];  var lastWeekRank = book.rank_last_week || ‘n/a’;  var weeksOnList = book.weeks_on_list || ‘New this week’;
```

```
  // ...
```

```
});
```

As we loop over each individual book, the variables are set to the data for their specific listing, which we’ll use when making the entry.

In the code listing above,

* the ISBN number is located within the book’s `isbns` array
* we select the 10-digit version of the ISBN number at `book_details[0]`
* the last week ranking is at `rank_last_week` and defaults to ‘n/a’
* the number of weeks it has been on the best sellers list, is at `weeks_on_list` and defaults to “New this week” for books that appear on the list for the first time

Next, we can make an HTML object to append to the `best-seller-titles` list. Be sure your project includes [jQuery](https://jquery.com/). On CodePen, you can go to settings and add it in the JavaScript panel.

```
var listing =   '<div id="' + book.rank + '" class="entry">' +     '<p>' +       '<img src="" class="book-cover" id="cover-' + book.rank + '">' +     '</p>' +     '<h2><a href="' + book.amazon_product_url + '" target="_blank">' + bookInfo.title + '</a></h2>' +    '<h4>By ' + bookInfo.author + '</h4>' +    '<h4 class="publisher">' + bookInfo.publisher + '</h4>' +    '<p>' + bookInfo.description + '</p>' +     '<div class="stats">' +      '<hr>' +       '<p>Last Week: ' + lastWeekRank + '</p>' +       '<p>Weeks on list: ' + weeksOnList + '</p>' +    '</div>' +  '</div>';
```

```
$('#best-seller-titles').append(listing);
```

Notice that the image is left blank. On [CodePen](https://codepen.io/agbales/pen/LNWPYW), I’ve added a placeholder image to fill in any undefined responses from Google.

Finally, we’ll can update the book rank number and pass along the rank and ISBN number to `updateCover()`.

```
$('#' + book.rank).attr('nyt-rank', book.rank);
```

```
updateCover(book.rank, isbn);
```

We can now write `updateCover()`, which will handle retrieving the thumbnail from the Google Books API.

### Google Books API

We’ve gathered the textual parts of the listing, but to add a book cover, one of the easiest ways I came across was to call upon the Google Books API. Be sure to grab an API Key from the [Google Books API](https://developers.google.com/books/).

Using the 10-digit ISBN number, we can get a thumbnail book cover image by again using `fetch()`. As before, we have to drill down into the object to find the single link referencing the thumbnail image we’re looking for:

```
function updateCover(id, isbn) {  fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn + "&key=" + apiKey, {    method: 'get'  })  .then(response => { return response.json(); })  .then(data => {    var img = data.items[0].volumeInfo.imageLinks.thumbnail;    img = img.replace(/^http:\/\//i, 'https://');    $('#cover-' + id).attr('src', img);  })    .catch(error=> {       console.log(error);  });}
```

After the image is secured, `replace()` swaps any HTTP links to secure HTTPS versions. We then update the book cover by selecting the proper cover ID and updating its image source.

### Style

I’ve added additional styles with SASS. If you’re more comfortable with CSS or SCSS, use the drop down button in that window to compile the code.

The last bit of JavaScript you’ll see controls the logo scaling. This code is triggered when the window scrolls. As the window scrolls down, the logo condenses from a height of 80px down to 35px.

```
$(window).scroll(function (event) {  var scroll = $(window).scrollTop();  if (scroll > 50) {    $(‘#masthead’).css({‘height’:’50', ‘padding’ : ‘8’});    $(‘#nyt-logo’).css({‘height’:’35'});  } else {    $(‘#masthead’).css({‘height’:’100', ‘padding’:’10'});    $(‘#nyt-logo’).css({‘height’:’80'});  }});
```

### Final Thoughts

It was exciting to return to a project and build on its features. While I may have approached this problem differently if I’d begun from scratch, this example shows a way to take a typical API call and add upon that work.

In fact, one reason I particularly wanted to share this project was remembering how frustrating it could get for me when I first started working with APIs. I’d get overwhelmed with the documentation, not sure which features or syntax were leading me in the right direction. I often wished for a clear example or walk-through of something a touch beyond the Hello World.

APIs each provide a specific service, and sometimes it’s necessary to combine them. This is just one way of bringing together multiple services, but I hope it’s a bit of inspiration for those exploring ways to combine APIs to create richer content.

