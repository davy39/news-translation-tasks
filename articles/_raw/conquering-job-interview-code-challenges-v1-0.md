---
title: How to Conquer Job Interview Coding Challenges
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-17T03:33:34.000Z'
originalURL: https://freecodecamp.org/news/conquering-job-interview-code-challenges-v1-0
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/le-tan-nsexDkLGC-c-unsplash.jpg
tags:
- name: challenge
  slug: challenge
- name: code
  slug: code
- name: code challenge
  slug: code-challenge
- name: coding
  slug: coding
- name: coding interview
  slug: coding-interview
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: interview
  slug: interview
- name: Interviewing
  slug: interviewing
- name: JavaScript
  slug: javascript
- name: job
  slug: job
- name: Job Hunting
  slug: job-hunting
- name: Job Interview
  slug: job-interview
- name: learn to code
  slug: learn-to-code
- name: learning to code
  slug: learning-to-code
seo_title: null
seo_desc: 'By Jonathan Sexton

  As many of you know, I have been applying for a job in web development for a few
  weeks and I thought it would be a good idea to share some of the coding challenges
  I''ve encountered.

  Not only that but I''ll share the ways I went abou...'
---

By Jonathan Sexton

As many of you know, I have been applying for a job in web development for a few weeks and I thought it would be a good idea to share some of the coding challenges I've encountered.

Not only that but I'll share the ways I went about solving these challenges.  Granted, there are many ways to solve these challenges but these are the ways I went about it.  If you have different ways that's awesome and I'd love for you to share them with me!

I will not share any identifiable information about the companies or specifics on the interview process of said company to preserve process integrity.

Alright, let's get to it then.

## The Challenge

This is a challenge I was given recently that I felt good about solving:

_**Task: Return a basic styled list of posts from an endpoint in reverse chronological order**_

To protect the company and their information, I will not share the URL from which I returned the information but instead will have a generic link from [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (a great, free, open source API for developers when you need to get some generic outside data) in the code below.

Here's the HTML I started with so we have something to display our results in:

![a code example showing HTML](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-3.png)
_Basic HTML boilerplate_

The _<ul>_ tag has an id so we can style it later in the process.

## Fetching Data From the Endpoint

Alright, let's dig into the **JavaScript** portion of this challenge.  First, I like to set my output and display variables:

![JavaScript code showing two variables being declared](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-4.png)
_Our variables used when displaying the returned code_

I use _let_ for the _output_ variable and set it to _null_ because we will change it's value later in the code.  The _list_ variable is declared with _const_ because it's value will not be changing.

![javascript code showing a fetch function](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-12.png)
_Fetching data from the endpoint_

In the above example, we’re declaring an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) named _getData_ wrapped in a [try…catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) block (This is a cleaner/easier to use/read syntax that uses _tries_ some code and _catches_ errors if they happen — you’ll also see the _catch_ portion below).  Because we're getting data asynchronously we also need to make use of _[async/await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)_ to fetch data.  This is the method I'm most comfortable with but I know there are many other ways to get data from an endpoint so feel free to share yours :D

Once we've declared our _data_ variable, the next thing is to set a variable to turn the returned data to a JSON object so we can get it in a usable form.  We do that with the _[.json()](https://developer.mozilla.org/en-US/docs/Web/API/Body/json)_ method.  We're awaiting the data as well because if we were to omit the _await_ keyword, JavaScript would try to turn the _data_ variable into JSON but the data would not be there yet because it's coming from an asynchronous API.

![a console log of a javascript array ](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-9.png)
_Our glorious data!_

As the very last line in the section, we _console.log_ our data that we get back from the API endpoint just to make sure we're getting everything we wanted.  We have an array full of objects.  You'll also notice that the key _published_at_ holds our dates and they are not in any type of order.  Their format is also not a simple four digit number representing the year which would make it easy to filter them into _**reverse chronological order**_.  We'll need to take care of that.

## Manipulating Our Data

![javascript code that's copying a variable](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-7.png)
_Making a copy of our data variable_

Here we declare the variable _dataCopy_ which points to the _dataJSON_ variable mutated into an array via the _[spread operator(...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)_.  Essentially, we are copying our returned JSON data so we aren't manipulating the original (bad practice) while making it into an array so that we can iterate over it.

After, we _[sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)_ the array.  Sort is an extremely useful array method that will put our array indices into the order of our choosing based on the function we pass into _sort._

Typically, we might want to sort the data based on value (largest to smallest) so we subtract the parameter _**a**_ from parameter _**b**_.  But because we need to display our results in _**reverse chronological order**_ I decided to produce a new date (accomplished with the _[new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)_ operator and the JavaScript built in method _[Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)_ that creates a new platform independent formatted instance of a date.  Now, because _**a**_ and _**b**_ represent our objects sitting inside our array indices, we can access the key/value pairs held within said objects.  So, we subtract _b.published_at_ from _a.published_at_ and this should give us our dates in _**reverse chronological order**_.

## Displaying the Fruits of Our Labor

Remember that _output_ variable we set to _null_ at the very top of our program?  Well now is it's time to shine!

![javascript code showing an output variable being changed](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-10.png)
_That output variable is earning it's keep now!_

So, there's a few things going on here.  First, we're setting our _output_ variable to a new value by mapping over our _dataCopy_ variable using the _[map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)_ method.  This method returns a new array with the results of calling the provided function once for each index.  The _item_ parameter represents our objects inside of our array that was returned from the endpoint and thus has access to all of their properties such as _title_ and _published_at_.

We return two list elements with a _<span>_ inside each one (for styling purposes), as well as a string for the **Title** and **Date Published** headings.  Inside of those, we have our variables that use [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) to set the title and the date for each post.

Then, we set our _list_ variable's _[innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)_ equal to that of our _output_ variable.

Finally, we have the closing bracket and error handling of our _try...catch_ block as well as our function call:

![javascript code showing error handling for a fetch request](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-11.png)
_This code will handle any errors and display them in the console_

## Final Code

Here is what our full code body looks like now:

![javascript code ](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-13.png)
_The entirety of our code base_

And here is our basic CSS styling:

![css code showing basic styling of an element](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-14.png)
_Did I say basic styling? I meant basic :D_

And here is the result of our work with it's very basic styling:

![a list of posts in reverse chronological order](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-15.png)
_Isn't it beautiful?_

As you can see, we accomplished what we set out to do and in fact the list is in _**reverse chronological order**_. Yay!

---

I hope you've enjoyed this walk through of my thought process and of how I solved this challenge.  Granted, there are many ways of completing this so feel free to share yours with me!  I'm excited to keep this series going and will post another after I've gone through another challenge!

Also, I cross post most of my articles on great platforms like [Dev.to](https://dev.to/jsgoose) and [Medium](https://medium.com/@joncsexton) so you can find my work there as well. This article was originally posted on my [blog](https://jonathansexton.me/blog) on May 27, 2019. 

While you’re here why not [sign up for my **Newsletter**](https://jonathansexton.me/blog/).  I promise I’ll never  spam your inbox and your information will not be shared with  anyone/site.  I like to occasionally send out interesting resources I  find, articles about web development, and a list of my newest posts.

Have an awesome day filled with love, joy, and coding!

