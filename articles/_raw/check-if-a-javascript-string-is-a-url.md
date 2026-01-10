---
title: How to Check if a JavaScript String is a Valid URL
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2022-06-24T15:09:54.000Z'
originalURL: https://freecodecamp.org/news/check-if-a-javascript-string-is-a-url
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/freecodecamp_new.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'A URL – or Uniform Resource Locator – is text used to identify resources
  like web pages, images, and videos on the internet.

  We commonly refer to URLs as website addresses, and they''re used for file transfer,
  emails, and other applications.

  URLs cons...'
---

A URL – or Uniform Resource Locator – is text used to identify resources like web pages, images, and videos on the internet.

We commonly refer to URLs as website addresses, and they're used for file transfer, emails, and other applications.

URLs consist of multiple parts – protocol, domain name, and so on – that tell the browser how and where to retrieve the resource.

In JavaScript, you may need to use a URL in the anchor tags or buttons to link the user to another webpage. This URL string must be verified to make sure it's a valid URL in such situations.

This tutorial will teach you some ways to check if a JavaScript string is a valid URL.

To learn how to get the current URL in JavaScript, you can read this article on [How to Get the Current URL in JavaScript](https://www.jsowl.com/how-to-get-the-current-url-in-javascript/).

## How to Check if a String is a Valid URL Using Regex

Regular expressions (regex) are patterns that match character combinations in a JavaScript string. In JavaScript, [regular expressions](https://www.freecodecamp.org/news/a-quick-and-simple-guide-to-javascript-regular-expressions-48b46a68df29/) are also known as objects that provide different methods to perform various operations.

You can construct a regular expression in two ways:

* Using regular expression literals
* Using regular expression constructors

**Note:** It is appropriate to use the regular expression method when you just want to check if a string is a valid URL and don't want any other additional objects created.

Let's learn how these two methods work.

### How to use regular expression literals

In a regular expression literal, the pattern is enclosed between the slashes, as you'll see below.

The pattern includes the validation of parts needed in the `URL`. For example, a protocol, `https`, a `//`, and so on.

```
const urlPattern = /(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;

```

### How to use a regular expression constructor

To create a regular expression using the construction method, use the `RegExp()` constructor and pass the pattern as a parameter.

```
const urlPattern = new RegExp('(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?');

```

To demonstrate how to validate if a string is a `URL`, let's create a method that will validate a JavaScript `String` using the regular expression constructor and return `True` or `False` based on the matched pattern.

```js
	const isValidUrl = urlString=> {
	  	var urlPattern = new RegExp('^(https?:\\/\\/)?'+ // validate protocol
	    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // validate domain name
	    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // validate OR ip (v4) address
	    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // validate port and path
	    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // validate query string
	    '(\\#[-a-z\\d_]*)?$','i'); // validate fragment locator
	  return !!urlPattern.test(urlString);
	}

```

### How to use regex to validate a URL string

The code below demonstrates how to validate different URL strings using the above method:

```js
	var url = "invalidURL";
	console.log(isValidUrl(url));      //false
	 
	var url = "htt//jsowl";            //false
	console.log(isValidUrl(url));
	
    var url = "www.jsowl.com";         //true
    console.log(isValidUrl(url));
    
    var url = "https://www.jsowl.com"; //true
    console.log(isValidUrl(url));
    
    var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
    console.log(isValidUrl(url));      //true

```

## How to Check if a String is a Valid URL using URL Constructor

You can use the URLConstructor to check if a string is a valid URL.

[URLConstructor](https://developer.mozilla.org/en-US/docs/Web/API/URL) (`new URL(url)`) returns a newly created URL object defined by the URL parameters.

A JavaScript [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError) exception is thrown if the given URL is not valid.

**Note:** It is appropriate to use this method when you want to construct a URL object in your program for further uses.

### URL Constructor Syntax

The following syntax explains how to create a URL Object with a JavaScript String.

```
new URL(url);
new URL(url, base);

```

Where,

* `url` is a string or any object with a [stringifier](https://developer.mozilla.org/en-US/docs/Glossary/Stringifier) that represents an absolute or relative URL. If **URL** is an absolute URL, **base** shall be ignored. If **URL** is a relative URL, **base** is required.
* `base` (optional) is a string representing the base URL. It must be passed when the URL is relative. Defaults to _undefined_ when ignored.

### Example of URL Constructor method

To demonstrate how the URL constructor method works, let's create a lambda function in JavaScript to construct a new URL with the passed string.

* If the string is a valid URL, a URL object is created, and `true` is returned
* If the String is not a valid URL, a `Tyeperror` exception is thrown, and `false` is returned

```
const isValidUrl = urlString=> {
      try { 
      	return Boolean(new URL(urlString)); 
      }
      catch(e){ 
      	return false; 
      }
  }

```

### How to use the `isValidURL()` method

Let's invoke the `isValidURL()` method for different string types and see the results.

```
  var url = "invalidURL";
  console.log(isValidUrl(url));     //false
  
  var url = "htt//jsowl";
  console.log(isValidUrl(url));     //false
  
  var url = "www.jsowl.com";
  console.log(isValidUrl(url));     //false
  
  var url = "tcp://www.jsowl.com";
  console.log(isValidUrl(url));     //true
  
  var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
  console.log(isValidUrl(url));     //true

```

In the first three cases, you can see that _an invalid URL string_ is passed. As a result, URL object creation fails with a `TypeError` and `false` is returned.

In the last two cases, _valid URL string_ is passed. So a `URL` object is created successfully, and `True` is returned, confirming the proper URL.

Let's see one more example to validate a specific URL part.

In this example, you are validating a specific protocol in the URL. The URL must contain the `http` or `https` protocol.

```
	const isValidUrl = urlString=> {
		let url;
		try { 
	      	url =new URL(urlString); 
	    }
	    catch(e){ 
	      return false; 
	    }
	    return url.protocol === "http:" || url.protocol === "https:";
	}

```

### Example of how to validate part of a URL

Let's invoke the `isValidURL()` method for different string types and protocols and see the results.

```
var url = "tcp://www.jsowl.com";
console.log(isValidUrl(url));      //false

var url = "https://www.jsowl.com";
console.log(isValidUrl(url));      //true

```

In the first case, the URL string _(tcp://www.jsowl.com)_ is valid, but it doesn't contain a specific protocol (`HTTP`/`HTTPS`). So it returns _false_.

In the second case, the URL string _[https://www.jsowl.com](https://www.jsowl.com)_ is _valid_ and contains the specific protocol. So it returns _true_.

## How to Check if a String is a Valid URL Using an Input Element

HTML supports an input element with type [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/url),  specifically for representing URL values.

The `<input>` element's `value` attribute containing the string is automatically validated by matching the URL syntax (_either has an empty or properly formed URL_) before the form can be submitted.

[`HTMLInputElement.checkValidity()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checkValidity) method is used to check if a string in  `<input>` element’s value attribute is `URL`. The `checkvalidity()` method returns `true` if the value is a proper URL and `false` if the input is not a proper URL.

Let's create a method which creates an input element type `URL` and validates the input using the `checkValidity()` method.

```
    const isValidUrl = urlString =>{
      var inputElement = document.createElement('input');
      inputElement.type = 'url';
      inputElement.value = urlString;

      if (!inputElement.checkValidity()) {
        return false;
      } else {
        return true;
      }
    } 

```

Now let's use this method and validate different strings to see if they are valid URLs.

```
    var url = "invalidURL";
    console.log(isValidUrl(url));     //false
    
    var url = "htt//jsowl";
    console.log(isValidUrl(url));     //false
    
    var url = "www.jsowl.com";
    console.log(isValidUrl(url));     //false
    
    var url = "https://www.jsowl.com";
    console.log(isValidUrl(url));     //true
    
    var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
    console.log(isValidUrl(url));     //true

```

This is how you can use the input type method to check if a string is a valid URL.

## How to Check if a String is a Valid URL Using the Anchor Tag Method

This section teaches you how to use the [HTMLAnchorElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement) to check whether a JavaScript string is a URL.

**Note:** It is appropriate to use this method when you want to assign a URL to the `anchor` tag of your webpage and ensure that the URL string is valid and gets assigned to the `anchor` tag properly.

The `HTMLAnchorElement` interface represents hyperlink elements. It provides special properties and methods for manipulating the layout and presentation of such elements. It is also called an anchor tag.

You can assign a URL to an anchor tag using the `href` attribute. While assigning,

* If a valid URL string is passed, it is assigned to the anchor tag
* If an invalid URL is passed, the [current browser location](https://www.jsowl.com/how-to-get-the-current-url-in-jquery/) is assigned to the anchor tag
* By default, the anchor tag will have an empty URL (“”)

Once the URL is assigned, you can extract a specific part of the URL using the attributes explained below.

<table>
<thead>
<tr>
<th>HTMLAnchorElement atribute</th>
<th>usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>host</code></td>
<td>a string representing hostname and port</td>
</tr>
<tr>
<td><code>hostname</code></td>
<td>a string representing hostname</td>
</tr>
<tr>
<td><code>href</code></td>
<td>a string containing a valid URL</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>returns a string containing the origin, its schema, domain name and port</td>
</tr>
<tr>
<td><code>port</code></td>
<td>a string representing the port if specified</td>
</tr>
<tr>
<td><code>protocol</code></td>
<td>a string representing the protocol including the trailing('<code>:</code>')</td>
</tr>
<tr>
<td><code>pathname</code></td>
<td>a string containing the path URL from initial (/) and not including the query string</td>
</tr>
</tbody>
</table>

Now, let's see how to check if the assigned string was a proper URL.

If it was a proper URL, it would be assigned to the anchor tag. Else, the current browser location will be assigned to the anchor tag.

So to check if it was a proper URL, you can check if the anchor tag’s `host` is NOT equal to the current location using the statement `a.host != window.location.host`.

Let's look at the code.

We create a lambda function and assign it to the constant `isValidUrl` in the code below.

The function creates an anchor tag element and assigns the URL string to the anchor tag. After that, it checks if the `host` attribute of the element is `null` or not defined.

If it is not null, it checks whether the `host` attribute is NOT equal to the current browser URL and returns `True` when it is not equal. 

This is because if the passed URL was valid, then the anchor tag will have the URL value. But if the passed URL was invalid, the anchor tag will have the current browser location. In this case, the lambda function returns `False`.

```
const isValidUrl = urlString =>{	
  	var a  = document.createElement('a');
   	a.href = urlString;
   	return (a.host && a.host != window.location.host);
  }

```

The below code snippets invoke the lambda function `isValidUrl()` with different inputs and print the output accordingly in the console.

```js
  var url = "invalidURL";
  console.log("1.AnchorTag:  " +isValidUrl(url));    //false
  
  var url = "htt//jsowl";
  console.log("22.AnchorTag:  "+isValidUrl(url));    //false
  
  var url = "www.jsowl.com";  
  console.log("3.AnchorTag:  " +isValidUrl(url));    //false  
  
  var url = "https://www.jsowl.com";  
  console.log("4.AnchorTag:  " +isValidUrl(url));    //true 
  
  var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
  console.log("5.AnchorTag:  " +isValidUrl(url));    //true 

```

This tutorial is available in [this](https://jsfiddle.net/jsowl/mvzqh4of/266/) JSFiddle.

## Conclusion

In this article, you've learned how to check if a JavaScript string is a `URL` using different methods and when it is appropriate to use each method.

If you liked this article, feel free to share it.

You can [check out my other tutorials on my blog, JS Owl](https://www.jsowl.com/).

