---
title: What is a JavaScript Object? Key Value Pairs and Dot Notation Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T22:04:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-javascript-object
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Blue--Violet-and-Orange-Shapes-Fitness-Influencer-YouTube-Thumbnail-Set--2--1.png
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: null
seo_desc: "By Danny Thompson\nObjects are one of the most valuable things you can\
  \ learn in JavaScript. You can use them to take your programs to the next level.\
  \ \nAn object is a collection of data – or key value pairs – which consist of variables\
  \ and functions th..."
---

By Danny Thompson

Objects are one of the most valuable things you can learn in JavaScript. You can use them to take your programs to the next level. 

An **object** is a collection of data – or key value pairs – which consist of variables and functions that you can access using dot notation.

Now that's a bunch of words that might not mean anything to you at the moment, so let's break it down. 

## What is a Key Value Pair in JavaScript? 

The easiest way to explain a key value pair is that you have 2 items that are linked together. One being the "key" and one being the "value". An object can have several Key Value Pairs inside of it. 

![An image of an object showing the relation between key and value.](https://www.freecodecamp.org/news/content/images/2021/07/Blue--Violet-and-Orange-Shapes-Fitness-Influencer-YouTube-Thumbnail-Set--3-.png)

Now that we understand what key value pairs are, we can dive deeper into objects.

## What is an Object in JavaScript? 

This is an object in JavaScript: 

```js
const phone = {
	brand: ['Samsung', 'Apple', 'Google'],
	quantity: [1,2,3],
	howManyGooglePhones: function(){
		alert("There are " + this.quantity[1] + ' ' + this.brand[2] + " phones available.");
	}
}

phone.howManyGooglePhones();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-35.png)

We create and name our object – in this case we have named it `phone`. We also have everything wrapped in our curly braces { }. Each key is separated from the value using a colon `:`.

In the code above, we have 2 arrays and one function. Notice how each key value pair ends with a comma `,` – this is very important and is required.

## What is Dot Notation in JavaScript?

Dot notation is where we can call that key value pair (which is known as a property) and pulls that information. 

If I wanted the brand Samsung I could do **`phone.brand[0]`** and it would give me Samsung. We use the object name (in this example it is `phone`), use a Dot, and then proceed by writing the name of the property.

Our function is set up to display how many phones we have of each brand. In the above function we are using it to show how many Google Phones we have in stock.

**`this.quantity[1]`** is accessing the "quantity" property and is looking in the [1] position for the value. **`this.brand[2]`** is accessing the Brand property that we want to show, which in this case is Google. 

Can you quickly figure out how we would access Apple with the quantity being 3? What would that look like in this situation?

`this` is being used because we want to access these values from within this object. The alert is creating a pop up to display this info when the program loads for this example.

Now that our object is complete, we want to call the function that is in the object and have it displayed. Since we are no longer in the object, **we will not be using `this`** like we did inside of the object. 

**Instead** we will be calling the object by name and using Dot notation. Our object name is **`phone`** so let's use it then the name of the function:

**`phone.howManyGooglePhones();`**

Calling the function will now create this pop up:

![Pop up alert shows that there are 2 Google Phones available.](https://www.freecodecamp.org/news/content/images/2021/07/image-34.png)

You successfully went through making an object, called a function, that was in the object that accessed 2 different values from the properties. Nice work!

If you like my blog articles you will love my social media posts.   
Follow me on Twitter @DThompsonDev

