---
title: How to Format Dates in JavaScript with One Line of Code
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2021-07-03T06:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-dates-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Formatting-Date-in-JavaScript-with-1-line-of-code.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'For a long time, I''ve used libraries like Date-fns whenever I need to
  format dates in JavaScript. But it gets really weird whenever I do this in small
  projects that require simple date formats which JavaScript offers by default.

  I discovered that mos...'
---

For a long time, I've used libraries like `Date-fns` whenever I need to format dates in JavaScript. But it gets really weird whenever I do this in small projects that require simple date formats which JavaScript offers by default.

I discovered that most developers do this a lot. And I thought that this was the best way until I recently figured out that **we don’t always need to use libraries** to format dates in JavaScript\*\*.\*\*

In case you are curious to try this out, here is the code:👇

```javascript
new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short", day:"numeric"}) 
// "Friday, Jul 2, 2021"
```

After trying this in your own code and seeing that it works, let's understand why it works and learn some other ways of formatting dates in JavaScript with just one line of code.

### Here's an Interactive Scrim about Formatting Dates in JavaScript with One Line of Code

<iframe src="https://scrimba.com/scrim/co6234e429a20cd020aceb3cc?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

# How to Format Dates in JS

Getting the date in JavaScript isn't usually a problem, but formatting these dates to suit your project can be cumbersome for beginners. Because of this, most people eventually end up using libraries.

The most used method to get the date in JavaScript is the `new Date()` object.

By default, when you run `new Date()` in your terminal, it uses your browser's time zone and displays the date as a full text string, like **Fri Jul 02 2021 12:44:45 GMT+0100 (British Summer Time).**

But having something like this in your web page or application is not professional and isn't easy to read. So this forces you to look for better ways to format these dates.

Let’s take a look at some methods that operate on a date object.

# Date Methods in JavaScript

There are so many methods that you can apply to the date object. You can use these methods to get information from a date object. Here are some of them:

* `getFullYear()` – gets the year as a four digit number (yyyy)
    
* `getMonth()` – gets the month as a number (0-11)
    
* `getDate()` – gets the day as a number (1-31)
    
* `getHours()` – gets the hour (0-23)
    

And lots more…

Unfortunately, most of these methods still needs a lot of code to convert the dates to the format we desire.

For example, `new Date().getMonth()` will output 6 which stands for **July.** For me to use July in my project, I will need to have long code like this which can really be cumbersome:

```javascript
const currentMonth = new Date();
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
console.log(months[currentMonth.getMonth()]);
```

Let’s take a look at two methods that you can use to format your dates in the best way so you can use them for your projects.

## The toDateString() Method in JavaScript

The JavaScript `toDateString()` method returns the date portion of a date object in the form of a string using the following format:

1. First three letters of the week day name
    
2. First three letters of the month name
    
3. Two digit day of the month, padded on the left a zero if necessary
    
4. Four digit year (at least), padded on the left with zeros if necessary
    

```javascript
new Date().toDateString();
//"Fri Jul 02 2021"
```

One major downside to this method is our inability to manipulate the date output the way we want it.

For example, it doesn’t give us the ability to show dates according to our language. Let’s take a look at another method which to me is still one of the best.

## The toLocaleDateString() Method in JavaScript

This method returns the date object as a string using local conventions. It also takes in options as arguments which lets you/your applications customize the behavior of the function.

**Syntax:**

```javascript
toLocaleDateString()
toLocaleDateString(locales)
toLocaleDateString(locales, options)
```

Let's take a look a some examples and their outputs:

```javascript
const currentDate = new Date();

const options = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };

console.log(currentDate.toLocaleDateString('de-DE', options));
//Freitag, 2. Juli 2021

console.log(currentDate.toLocaleDateString('ar-EG', options))
// الجمعة، ٢ يوليو ٢٠٢١

console.log(currentDate.toLocaleDateString('en-us', options));
//Friday, Jul 2, 2021
```

You can also decide not to use either locales or options:

```javascript
new Date().toLocaleDateString()
// "7/2/2021"
```

And you can also decide to only use locales. This will output the same information as the previous based on my browser's time zone.

```javascript
new Date().toLocaleDateString('en-US')
"7/2/2021"
```

You can also decide to twist the options as you wish. There are 4 basic options which are:

* `weekday` – This outputs the day of the week depending on how you want it to appear (short or long).
    
* `year` – This outputs the year as a number
    
* `month` – This outputs the month of the year depending on how you want it to appear (short or long).
    
* `day` – Finally, this outputs the day as a number
    

```javascript
new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short"}) // "Jul 2021 Friday"

new Date().toLocaleDateString('en-us', { year:"numeric", month:"short"})
// "Jul 2021"
```

# Conclusion

The date object has about seven formatting methods. Each of these methods gives you a specific value:

1. `toString()` gives you **Fri Jul 02 2021 14:03:54 GMT+0100 (British Summer Time)**
    
2. `toDateString()` gives you **Fri Jul 02 2021**
    
3. `toLocaleString()` gives you **7/2/2021, 2:05:07 PM**
    
4. `toLocaleDateString()` gives you **7/2/2021**
    
5. `toGMTString()` gives you **Fri, 02 Jul 2021 13:06:02 GMT**
    
6. `toUTCString()` gives you **Fri, 02 Jul 2021 13:06:28 GMT**
    
7. `toISOString()` gives you **2021-07-02T13:06:53.422Z**
    

If you are looking for more advanced date formats, then you will need to create a custom format yourself. Check out the resources below to help you understand how to create custom date formats.

## Useful Resources

* [Everything You Need to Know About Date in JavaScript](https://css-tricks.com/everything-you-need-to-know-about-date-in-javascript/)
    
* [JavaScript - How to Format Date in JavaScript](https://www.tabnine.com/academy/javascript/how-to-format-date/)
    
* [How to format a date in JavaScript](https://flaviocopes.com/how-to-format-date-javascript/)
    
* [The Definitive Guide to DateTime Manipulation](https://www.toptal.com/software/definitive-guide-to-datetime-manipulation)
