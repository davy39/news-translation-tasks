---
title: The Best jQuery Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-23T00:23:00.000Z'
originalURL: https://freecodecamp.org/news/the-best-jquery-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f1b740569d1a4ca40dc.jpg
tags:
- name: jQuery
  slug: jquery
seo_title: null
seo_desc: 'jQuery is the most widely-used JavaScript library, and is used in more
  than half of all major websites. It''s motto is "write less, do more...!"

  jQuery makes web development easier to use by providing a number of ''helper'' functions.
  These help develop...'
---

jQuery is the most widely-used JavaScript library, and is used in more than half of all major websites. It's motto is "write less, do more...!"

jQuery makes web development easier to use by providing a number of 'helper' functions. These help developers to quickly write DOM (Document Object Model) interactions without needing to manually write as much JavaScript themselves.

jQuery adds a global variable with all of the libraries methods attached. The naming convention is to have this global variable as `$`. by typing in `$.` you have all the jQuery methods at your disposal.

## Getting Started

There are two main ways to start using jQuery:

* **Include jQuery locally**: Download the jQuery library from [jquery.com](https://jquery.com/) and include it in your HTML code.
* **Use a CDN**: Link to the jQuery library using a CDN (Content Delivery Network).

```html
<head>
  <script src="/jquery/jquery-3.4.1.min.js"></script>
  <script src="js/scripts.js"></script>
</head>
```

```html
<head>
  <script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="js/scripts.js"></script>
</head>
```

## Selectors

jQuery uses CSS-style selectors to select parts, or elements, of an HTML page. It then lets you do something with the elements using jQuery methods, or functions.

To use one of these selectors, type a dollar sign and parentheses after it: `$()`. This is shorthand for the `jQuery()` function. Inside the parentheses, add the element you want to select. You can use either single- or double-quotes. After this, add a dot after the parentheses and the method you want to use.

In jQuery, the class and ID selectors are like those in CSS.

Here's an example of a jQuery method that selects all paragraph elements, and adds a class of "selected" to them:

```javascript
<p>This is a paragraph selected by a jQuery method.</p>
<p>This is also a paragraph selected by a jQuery method.</p>

$("p").addClass("selected");
```

In jQuery, the class and ID selectors are the same as in CSS. If you want to select elements with a certain class, use a dot (`.`) and the class name. If you want to select elements with a certain ID, use the hash symbol (`#`) and the ID name. Note that HTML is not case-sensitive, therefore it is best practice to keep HTML markup and CSS selectors lowercase.

### Selecting by class

If you want to select elements with a certain class, use a dot (.) and the class name.

```html
<p class="pWithClass">Paragraph with a class.</p>
```

```javascript
$(".pWithClass").css("color", "blue"); // colors the text blue
```

You can also use the class selector in combination with a tag name to be more specific.

```html
<ul class="wishList">My Wish List</ul>`<br>
```

```javascript
$("ul.wishList").append("<li>New blender</li>");
```

### Selecting by ID

If you want to select elements with a certain ID value, use the hash symbol (#) and the ID name.

```html
<li id="liWithID">List item with an ID.</li>
```

```javascript
$("#liWithID").replaceWith("<p>Socks</p>");
```

As with the class selector, this can also be used in combination with a tag name.

```html
<h1 id="headline">News Headline</h1>
```

```javascript
$("h1#headline").css("font-size", "2em");
```

### Selecting by attribute value

If you want to select elements with a certain attribute, use `([attributeName="value"])`.

```html
<input name="myInput" />
```

```javascript
$("[name='myInput']").value("Test"); // sets input value to "Test"
```

You can also use the attribute selector in combination with a tag name to be more specific.

```html
<input name="myElement" />`<br>
<button name="myElement">Button</button>
```

```javascript
$("input[name='myElement']").remove(); // removes the input field not the button
```

### Selectors that act as filters

There are also selectors that act as filters - they will usually start with colons. For example, the `:first` selector selects the element that is the first child of its parent. Here's an example of an unordered list with some list items. The jQuery selector below the list selects the first `<li>` element in the list--the "One" list item--and then uses the `.css` method to turn the text green.

```html
   <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
   </ul>
```

```javascript
$("li:first").css("color", "green");
```

### Attribute Selector

There are selectors that return elements which matches certain combinations of Attributes like _Attribute contains_, _Attribute ends with_, _Attribute starts with_ etc. Here's an example of an unordered list with some list items. The jQuery selector below the list selects the `<li>` element in the list--the "One" list item as it has `data*` attribute as `"India"` as its value--and then uses the `.css` method to turn the text green.

```html
   <ul>
      <li data-country="India">Mumbai</li>
      <li data-country="China">Beijing</li>
      <li data-country="United States">New York</li>
   </ul>
```

```javascript
$("li[data-country='India']").css("color", "green");
```

Another filtering selector, `:contains(text)`, selects elements that have a certain text. Place the text you want to match in the parentheses. Here's an example with two paragraphs. The jQuery selector takes the word "Moto" and changes its color to yellow.

```html
    <p>Hello</p>
    <p>World</p>
```

```javascript
$("p:contains('World')").css("color", "yellow");
```

Similarly, the `:last` selector selects the element that is the last child of its parent. The jQuery selector below selects the last `<li>` element in the list--the "Three" list item--and then uses the `.css` method to turn the text yellow.

`$("li:last").css("color", "yellow");`

**Note:** In the jQuery selector, `World` is in single-quotes because it is already inside a pair of double-quotes. Always use single-quotes inside double-quotes to avoid unintentionally ending a string.

### Multiple Selectors

In jQuery, you can use multiple selectors to apply the same changes to more than one element, using a single line of code. You do this by separating the different ids with a comma. For example, if you want to set the background color of three elements with ids cat,dog,and rat respectively to red, simply do:

```text
$("#cat,#dog,#rat").css("background-color","red");
```

## HTML Method

The jQuery `.html()` method gets the content of a HTML element or sets the content of an HTML element.

### Getting

To return the content of a HTML element, use this syntax:

```javascript
$('selector').html();
```

For example:

```javascript
$('#example').html();
```

### Setting

To set the content of a HTML element, use this syntax:

```javascript
$('selector').html(content);
```

For example:

```javascript
$('p').html('Hello World!');
```

That will set the content of all of the `<p>` elements to Hello World!

### Warning

`.html()` method is used to set the element's content in **HTML** format. This may be dangerous if the content is provided by user. Consider using `.text()` method instead if you need to set non-HTML strings as content.

## CSS Method

The jQuery `.css()` method gets the value of a computed style property for the first element in the set of matched elements or set one or more CSS properties for every matched element.

### Getting

To return the value of a specified CSS property, use the following syntax:

```js
    $(selector).css(propertyName);
```

Example:

```js
    $('#element').css('background');
```

Note: Here we can use any css selector eg: element(HTML Tag selector), .element(Class Selector), #element(ID selector).

### Setting

To set a specified CSS property, use the following syntax:

```js
    $(selector).css(propertyName,value);
```

Example:

```js
    $('#element').css('background','red');
```

To set multiple CSS properties, you'll have to use the object literal syntax like this:

```js
    $('#element').css({
        'background': 'gray',
        'color': 'white'
    });
```

If you want to change a property labeled with more than one word, refer to this example:

To change `background-color` of an element

```js
    $('#element').css('background-color', 'gray');
```

## Click Method

The jQuery Click method triggers a function when an element is clicked. The function is known as a "handler" because it handles the click event. Functions can impact the HTML element that is bound to the click using the jQuery Click method, or they can change something else entirely. The most-used form is:

```javascript
$("#clickMe").click(handler)
```

The click method takes the handler function as an argument and executes it every time the element `#clickMe` is clicked. The handler function receives a parameter known as an [eventObject](http://api.jquery.com/Types/#Event) that can be useful for controlling the action.

### Examples

This code shows an alert when a user clicks a button:

```html
<button id="alert">Click Here</button>
```

```javascript
$("#alert").click(function () {
  alert("Hi! I'm an alert");
});
```

The [eventObject](http://api.jquery.com/Types/#Event) has some built in methods, including `preventDefault()`, which does exactly what it says - stops the default event of an element. Here we pevent the anchor tag from acting as a link:

```html
<a id="myLink" href="www.google.com">Link to Google</a>
```

```javascript
$("#myLink").click(function (event) {
  event.preventDefault();
});
```

### More ways to play with the click method

The handler function can also accept additional data in the form of an object:

```javascript
jqueryElement.click(usefulInfo, handler)
```

The data can be of any type.

```javascript
$("element").click({firstWord: "Hello", secondWord: "World"}, function(event){
    alert(event.data.firstWord);
    alert(event.data.secondWord);
});
```

Invoking the click method without a handler function triggers a click event:

```javascript
$("#alert").click(function () {
  alert("Hi! I'm an alert");
});

$("#alert").click();
```

Now, whenever the page loads, the click event will be triggered when we enter or reload the page, and show the assigned alert.

Also you should prefer to use `.on("click",...)` over `.click(...)` because the former can use less memory and work for dynamically added elements.

### Common Mistakes

The click event is only bound to elements currently in the DOM at the time of binding, so any elements added afterwards will not be bound. To bind all elements in the DOM, even if they will be created at a later time, use the `.on()` method.

For example, this click method example:

```javascript
$("element").click(function() {
  alert("I've been clicked!");
});
```

Can be changed to this on method example:

```javascript
$(document).on("click", "element", function() {
  alert("I've been clicked!");
});
```

### Getting The Element From A Click event

This applies to both jQuery and plain JavaScript, but if you set up your event trigger to target a class, you can grab the specific element that triggered the element by using the `this` keyword.

jQuery happens to make it very easy (and multi browser friendly) to traverse the DOM to find that element's parents, siblings, and children, as well.

Let's say I have a table full of buttons and I want to target the row that button is in, I can simply wrap `this` in a jQuery selector and then get its `parent` and its parent's `parent` like so:

```javascript
$( document ).on("click", ".myCustomBtnClassInATable", function () {
    var myTableCell = $(this).parent();
    var myTableRow = myTableCell.parent();
    var myTableBody = myTableRow.parent();
    var myTable = myTableBody.parent();
    
    //you can also chain these all together to get what you want in one line
    var myTableBody = $(this).parent().parent().parent();
});
```

It is also interesting to check out the event data for the click event, which you can grab by passing in any variable name to the function in the click event. You'll most likely see an `e` or `event` in most cases:

```javascript
$( document ).on("click", ".myCustomBtnClassInATable", function (e) { 
    //find out more information about the event variable in the console
    console.log(e);
});
```

## Mousedown Method

The mousedown event occurs when the left mouse button is pressed. To trigger the mousedown event for the selected element, use this syntax: `$(selector).mousedown();`

Most of the time, however, the mousedown method is used with a function attached to the mousedown event. Here's the syntax: `$(selector).mousedown(function);` For example:

```text
$(#example).mousedown(function(){
   alert("Example was clicked");
});
```

That code will make the page alert "Example was clicked" when #example is clicked.

## Hover Method

The jquery hover method is a combination of the `mouseenter` and `mouseleave` events. The syntax is this:

```text
$(selector).hover(inFunction, outFunction);
```

The first function, inFunction, will run when the `mouseenter` event occurs. The second function is optional, but will run when the `mouseleave` event occurs. If only one function is specified, the other function will run for both the `mouseenter` and `mouseleave` events. Below is a more specific example.

```text
$("p").hover(function(){
    $(this).css("background-color", "yellow");
}, function(){
    $(this).css("background-color", "pink");
});
```

So this means that hover on paragraph will change its background color to yellow and the opposite will change back to pink.

## Animate Method

jQuery's animate method makes it easy to create simple animations using only a few lines of code. The basic structure is as following:

```javascript
$(".selector").animate(properties, duration, callbackFunction());
```

For the `properties` argument, you need to pass a javascript object with the CSS properties you want to animate as keys and the values you want to animate to as values. For the `duration`, you need to input the amount of time in milliseconds the animation should take. The `callbackFunction()` is executed once the animation has finished.

### Example

A simple example would look like this:

```javascript
$(".awesome-animation").animate({
	opacity: 1,
	bottom: += 15
}, 1000, function() {
	$(".different-element").hide();
});
```

## Hide Method

In its simplest form, **.hide()** hides the matched element immediately, with no animation. For example:

```javascript
$(".myclass").hide()
```

will hide all the elements whose class is _myclass_. Any jQuery selector can be used.

### .hide() as an animation method

Thanks to its options, **.hide()** can animate the width, height, and opacity of the matched elements simultaneously.

* Duration can be provided in milliseconds, or using the literals slow (600 ms) and fast(200ms). for example:
* A function can be specified to be called once the animation is complete, once per every matched element. This callback is mainly useful for chaining together different animations. For example

```javascript
$("#myobject").hide(800)
```

```javascript
$("p").hide( "slow", function() {
  $(".titles").hide("fast");
  alert("No more text!");
});
```

## Show Method

In its simplest form, **.show()** displays the matched element immediately, with no animation. For example:

```javascript
$(".myclass").show();
```

will show all the elements whose class is _myclass_. Any jQuery selector can be used.

However, this method does not override `!important` in the CSS style, such as `display: none !important`.

### .show() as an animation method

Thanks to its options, **.show()** can animate the width, height, and opacity of the matched elements simultaneously.

* Duration can be provided in milliseconds, or using the literals slow (600 ms) and fast(200ms). for example:
* A function can be specified to be called once the animation is complete, once per every matched element. for example

```javascript
$("#myobject").show("slow");
```

```javascript
$("#title").show( "slow", function() {
  $("p").show("fast");
});
```

## jQuery Toggle method

To show / hide elements you can use `toggle()` method. If element is hidden `toggle()` will show it and vice versa. Usage:

```javascript
$(".myclass").toggle()
```

## Slide Down method

This method animates the height of the matched elements. This causes lower parts of the page to slide down, making way for the revealed items. Usage:

```javascript
$(".myclass").slideDown(); //will expand the element with the identifier myclass for 400 ms.
$(".myclass").slideDown(1000); //will expand the element with the identifier myclass for 1000 ms.
$(".myclass").slideDown("slow"); //will expand the element with the identifier myclass for 600 ms.
$(".myclass").slideDown("fast"); //will expand the element with the identifier myclass for 200 ms.
```

## Load Method

The load() method loads data from a server and puts the returned data into the selected element.

**Note:** There is also a jQuery Event method called load. Which one is called, depends on the parameters.

### Example

```javascript
$("button").click(function(){
    $("#div1").load("demo_test.txt");
});
```

## Chaining

jQuery chaining allows you to execute multiple methods on the same jQuery selection, all on a single line.

Chaining allows us to turn multi-line statements:

```javascript
$('#someElement').removeClass('classA');
$('#someElement').addClass('classB');
```

Into a single statement:

```javascript
$('#someElement').removeClass('classA').addClass('classB');
```

## Ajax Get Method

Sends an asynchronous http GET request to load data from the server. Its general form is:

```javascript
jQuery.get( url [, data ] [, success ] [, dataType ] )
```

* `url`: The only mandatory parameter. This string contains the address to which to send the request. The returned data will be ignored if no other parameter is specified.
* `data`: A plain object or string sent to the server with the request.
* `success`: A callback function executed if the request succeeds. It takes as an argument the returned data. It is also passed the text status of the response.
* `dataType`: The type of data expected from the server. The default is Intelligent Guess (xml, json, script, text, html). If this parameter is provided, the success callback also must be provided.

### Examples

Request `resource.json` from the server, send additional data, and ignore the returned result:

```javascript
$.get('http://example.com/resource.json', {category:'client', type:'premium'});
```

Request `resource.json` from the server, send additional data, and handle the returned response (json format):

```javascript
$.get('http://example.com/resource.json', {category:'client', type:'premium'}, function(response) {
     alert("success");
     $("#mypar").html(response.amount);
});
```

However, `$.get` doesn't provide any way to handle error.

The above example (with error handling) can also be written as:

```javascript
$.get('http://example.com/resource.json', {category:'client', type:'premium'})
     .done(function(response) {
           alert("success");
           $("#mypar").html(response.amount);
     })
     .fail(function(error) {
           alert("error");
           $("#mypar").html(error.statusText);
     });
```

### Ajax GET Equivalent

`$.get( url [, data ] [, success ] [, dataType ] )` is a shorthand Ajax function, equivalent to:

```javascript
$.ajax({
     url: url,
     data: data,
     success: success,
     dataType: dataType
});
```

## Ajax Post Method

Sends an asynchronous http POST request to load data from the server. Its general form is:

```javascript
jQuery.post( url [, data ] [, success ] [, dataType ] )
```

* url : This is the only mandatory parameter. This string contains the adress to which to send the request. The returned data will be ignored if no other parameter is specified
* data : A plain object or string that is sent to the server with the request.
* success : A callback function that is executed if the request succeeds. It takes as an argument the returned data. It is also passed the text status of the response.
* dataType : The type of data expected from the server. The default is Intelligent Guess (xml, json, script, text, html). if this parameter is provided, then the success callback must be provided as well.

#### Examples

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'});
```

requests `form.php` from the server, sending additional data and ignoring the returned result

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'}, function(response){ 
      alert("success");
      $("#mypar").html(response.amount);
});
```

requests `form.php` from the server, sending additional data and handling the returned response (json format). This example can be written in this format:

```javascript
$.post('http://example.com/form.php', {category:'client', type:'premium'}).done(function(response){
      alert("success");
      $("#mypar").html(response.amount);
});
```

The following example posts a form using Ajax and put results in a div

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>jQuery.post demo</title>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
 
<form action="/" id="searchForm">
  <input type="text" name="s" placeholder="Search...">
  <input type="submit" value="Search">
</form>
<!-- the result of the search will be rendered inside this div -->
<div id="result"></div>
 
<script>
// Attach a submit handler to the form
$( "#searchForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    term = $form.find( "input[name='s']" ).val(),
    url = $form.attr( "action" );
 
  // Send the data using post
  var posting = $.post( url, { s: term } );
 
  // Put the results in a div
  posting.done(function( data ) {
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
  });
});
</script>
 
</body>
</html>
```

The following example use the github api to fetch the list of repositories of a user using jQuery.ajax() and put results in a div

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>jQuery Get demo</title>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
 
<form id="userForm">
  <input type="text" name="username" placeholder="Enter gitHub User name">
  <input type="submit" value="Search">
</form>
<!-- the result of the search will be rendered inside this div -->
<div id="result"></div>
 
<script>
// Attach a submit handler to the form
$( "#userForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    username = $form.find( "input[name='username']" ).val(),
    url = "https://api.github.com/users/"+username+"/repos";
 
  // Send the data using post
  var posting = $.post( url, { s: term } );
 
  //Ajax Function to send a get request
  $.ajax({
    type: "GET",
    url: url,
    dataType:"jsonp"
    success: function(response){
        //if request if made successfully then the response represent the data

        $( "#result" ).empty().append( response );
    }
  });
  
});
</script>
 
</body>
</html>
```

### Ajax POST Equivalent

`$.post( url [, data ] [, success ] [, dataType ] )` is a shorthand Ajax function, equivalent to:

```javascript
$.ajax({
  type: "POST",
  url: url,
  data: data,
  success: success,
  dataType: dataType
});
```


