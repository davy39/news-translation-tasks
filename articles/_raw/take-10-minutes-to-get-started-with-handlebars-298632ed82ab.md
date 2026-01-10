---
title: Take 10 minutes to get started with Handlebars
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T22:37:29.000Z'
originalURL: https://freecodecamp.org/news/take-10-minutes-to-get-started-with-handlebars-298632ed82ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hKdDzlUz__kgb46lJRJ6jA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Wing Puah

  Nowadays front-end development is no longer about building static HTML markup and
  compiling SASS files. The rise of Single Page Applications (SPAs) means we can do
  a lot of the rendering logic on the client-side. Modern day web developme...'
---

By Wing Puah

Nowadays front-end development is no longer about building static HTML markup and compiling SASS files. The rise of Single Page Applications (SPAs) means we can do a lot of the rendering logic on the client-side. Modern day web development often require dynamic data input.

While [React.js](https://reactjs.org/) is great, often it requires a learning curve for the developers before they can integrate it into the team. Recently, I was tasked with building the front-end of a course website. That marked the start of my exploration into [Handlebars.js](https://handlebarsjs.com/).

Handlebars is a popular and simple templating engine that is simple to use. It looks a lot like regular HTML, with embedded handlebars expressions in the curly braces {{}}.

```
<div class="entry">   <h1>{{name}}</h1>   <div>{{quote}}</div> </div>
```

Before we move on to the details of Handlebars, let’s see how data will be inserted into the page through vanilla Javascript. We will take the example of building a webpage that lists a few quotes. Because, hey, everyone needs some inspiration.

### Vanilla javascript

#### **Data retrieval**

Most of the time, you might be retrieving data via ajax, but for simplicity, we will create our own data object.

```
// quotes.js var quotes = [   {name: "Frank Lloyd Wright", quote: "You can use an eraser on the drafting table or a sledge hammer on the construction site."},  {name: "Douglas Adams", quote: "The major difference between a thing that might go wrong and a thing that cannot possibly go wrong is that when a thing that cannot possibly go wrong goes wrong it usually turns out to be impossible to get at or repair."},   {name: "Ettore Sottsass", quote: "I try and be as stupid as possible regarding my profession, which means I try to look at as few design magazines as possible."},   {name: "Shaun White", quote: "I’m a big fan of doing what you are really bad at. A lot."} ]
```

#### **Create HTML markup**

```
// index.html<div class="container>  <div class="row" id="quotes">  </div></div>
```

#### **Adding the data with Javascript**

We will use a _for_ loop to loop through the content above.

```
//quotes.jslet quoteMarkup = '';
```

```
for (var i = 0; i < quotes.length; i++) {  let name = quotes[i].name,       quote = quotes[i].quote;
```

```
quoteMarkup += '<div class="col-12 col-sm-6">' +                  '<h5>' + name + '</h5>' +                  '<p>' + quote + '</p>'                 '</div>'}
```

```
document.getElementById('quotes').innerHTML = quoteMarkup;
```

With code like this, it is difficult to read and tedious to write. And the HTML markup for this page now resides in both the index.html and quotes.js.

### Enter handlebars

#### **Getting started**

To start off, we need to include the Handlebar source code file. You can add the link inside the head tag or before the end of <body>.

```
&lt;script src="js/handlebars.js">&lt;/script>
```

Alternatively, you can also link to Handlebars from a CDN.

```
<script src="//cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.12/handlebars.min.js"></script>
```

#### **Create the template**

We will still use the data object of quotes from the file above. We will sprinkle some Handlebars magic on the index.html file.

```
//index.html<div class="container>  <div id="quotes">
```

```
<script id="quotes-template" type="text/x-handlebars-template">                  <div class="row">                    {{#each this}}                      <div class="col-12 col-sm-6 p-3">                          <div class="card">                              <h4 class="card-header">                                  {{name}}                              </h4>                              <div class="card-body">                                  {{quote}}                         </div>                          </div>                     </div>                    {{/each}}                </div>            </script>    </div></div>
```

* _each_: Iterates through the data
* _this_: _R_eferences to the current context.
* _text/x-handlebars-template_: To tell the browser not to execute the script as normal Javascript.

#### **Compile the template with Handlebars**

It only takes a few lines to compile the data with Handlebars. That is what I love about it. Even if someone on the team has not used Handlebars before, the script and markup are very simple for them to understand and pick up.

```
let content = document.getElementById('quotes'),    src = document.getElementById('quotes-template').innerHTML,     template = Handlebars.compile(src),            html = template(quotes);
```

```
content.innerHTML = html;
```

* _content_: Returns the element into which you want to insert the compiled information.
* _src_: Retrieves the markup of the template.
* _Handlebars.compile(src)_: Compiles the template in use. It will return a function that the data can be passed to so it can be be rendered.
* _template(quotes)_: Compiles the data into the template.
* _content.innerHTML_: Renders the above to the DOM

You can view [the project here](https://wing-puah.github.io/learn_handlebars/).

### Bonus

I used Handlebars for a multiple-templates website. I found myself writing the same ajax and Handlebars code multiple times. So, here are the two functions that I created to make my life easier.

#### **Getting data from ajax with Javascript**

```
function ajaxGet(url, callback) {    let xmlhttp = new XMLHttpRequest();    xmlhttp.onreadystatechange = function() {        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {            // console.log(xmlhttp.responseText);            try {                var data = JSON.parse(xmlhttp.responseText);            } catch(err) {                console.log(err.message +' Getting: ' + url);                return;            }            callback(data);        }    };
```

```
xmlhttp.open("GET", url, true);    xmlhttp.send();}
```

#### **Function to run Handlebars**

```
function runHandlebars(id, dataSrc, src) {  if(document.getElementById(id) != null) {    let content = document.getElementById(id);    ajaxGet(dataSrc, function(data){      let source = document.getElementById(src).innerHTML,           template = Handlebars.compile(source);
```

```
content.innerHTML = template(data);    });  }}
```

With these two functions, I could run all my Handlebars code on a single Javascript file. It will look something like this.

```
runHandlebars('nav-sub-1', '/data/courses.json', 'nav-submenu-template');
```

```
runHandlebars('contributors', '/data/contributors.json', 'contributors-template');
```

### Conclusion

My experience with Handlebars has been a positive one. In my project, I use it with gulp and metalsmith. Will I use it for other projects? My take is I prefer something like React or a full fledged static site generator like Jekyll. But in this case, when the team is more comfortable with HTML markup and it is a relatively simple website, Handlebars is a good choice.

