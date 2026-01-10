---
title: How to Format a Number as Currency in JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-03T15:29:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-number-as-currency-in-javascript-one-line-of-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--2-.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re working with data from an API or an external resource, you''ll
  get these data in some general format. For example, if you are building a store,
  you might have data like price.

  This price data might be in the form of a general number such a...'
---

When you're working with data from an API or an external resource, you'll get these data in some general format. For example, if you are building a store, you might have data like price.

This price data might be in the form of a general number such as 14340 or any other number as seen in the array below:

```js
const books = [
    {
        "id": 001,
        "name": "Clean Code",
        "price": 10.99,
    },
    {
        "id": 002,
        "name": "Introduction to Algorithms",
        "price": 1199,
    },
    {
        "id": 003,
        "name": "Programming Pearls",
        "price": 1.05,
    },
    {
        "id": 004,
        "name": "Program or Be Programmed",
        "price": 14340,
    }
]
```

You don't want to pass in numbers directly into your application or web page because they'll be difficult for the readers and users to understand.

Even if you add a currency sign, it doesn’t fix the problem because you would want to add commas and decimals in the correct positions. You’d also want each price output based on the currency with proper formatting.

For example, 14340 would be $14,340.00 (US Dollars) or ₹14,340.00 (Rupees) or €14.340,00 (Euross) and so on, depending on your defined currency, locale, and style. And you can convert these numbers into currencies using the `Intl.NumberFormat()` method in JavaScript.

In case you are in a rush, here is a basic example of what the code will look like:

```js
const price = 14340;

// Format the price above to USD using the locale, style, and currency.
let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

console.log(`The formated version of ${price} is ${USDollar.format(price)}`);
// The formated version of 14340 is $14,340.00
```

In this article, I'll help you understand each of the above options, what they do, and how to properly use this method to format a number as currency.

## How to Use the `Intl.NumberFormat()` Constructor to Format Numbers as Currency

You can use the `Intl.NumberFormat()` constructor to create `Intl.NumberFormat` objects that enable language-sensitive number formatting, such as currency formatting.

This constructor takes in two major parameters, `locales` and `options`. They're both optional.

```js
new Intl.NumberFormat(locales, options)

// Or

Intl.NumberFormat(locales, options)
```

**Note** that `Intl.NumberFormat()` can be called with or without `new`. Both will create a new `Intl.NumberFormat` instance.

When you use the `Intl.NumberFormat()` constructor without passing any locale or option, it will only format the number by adding commas.

```js
const price = 14340;
console.log(new Intl.NumberFormat().format(price)); // 14,340
```

You are not after regular number formatting, as seen above. You want to format these numbers as currency – so it returns the currency symbol with proper formatting without having to concatenate manually.

Let’s now explore both parameters.

### The First Argument: Locales

The locale is an optional parameter that can be passed as a string. It represents a specific geographical, political, or cultural region. It just formats the number based on the locale and is not the currency formatting.

```js
const price = 143450;

console.log(new Intl.NumberFormat('en-US').format(price)); // 143,450
console.log(new Intl.NumberFormat('en-IN').format(price)); // 1,43,450
console.log(new Intl.NumberFormat('en-DE').format(price)); // 143.450
```

You will notice that the numbers or prices are now formatted locally based on the locale. Let’s now explore the options parameter to customize the numbers as a currency.

### The Second Argument: Options (Style, Currency, …)

This is the main parameter and you can use it to apply more formatting like that of currency. This is a JavaScript object that holds other parameters like:

* `style`: You use this to specify the type of formatting you want. This takes in values like decimals, currency, and units. For this article, you will use **currency** because that is the style in which you want to format the number.
    
* `currency`: Another option is currency. You can use this option to specify the currency you want to format to, such as `'USD'`, `'CAD'`, `'GBP``'`, `'INR'` and lots more. This will also help provide the symbol in the appropriate position based on the locale.
    

```js
// format number to US dollar
let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

// format number to British pounds
let pounds = Intl.NumberFormat('en-GB', {
    style: 'currency',
    currency: 'GBP',
});

// format number to Indian rupee
let rupee = new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
});

// format number to Euro
let euro = Intl.NumberFormat('en-DE', {
    style: 'currency',
    currency: 'EUR',
});

console.log('Dollars: ' + USDollar.format(price));
// Dollars: $143,450.00

console.log(`Pounds: ${pounds.format(price)}`);
// Pounds: £143,450.00

console.log('Rupees: ' + rupee.format(price));
// Rupees: ₹1,43,450.00

console.log(`Euro: ${euro.format(price)}`);
// Euro: €143,450.00
```

There are other options you’ll most likely never use or change, such as `useGrouping`, which is used to group the number using commas (or periods, for some locales). This is a boolean field – by default, it is set to `true`. This is why your output has had a comma or period in this article (like $143,450.00).

When you set its value to `false`, you will notice there is no more grouping:

```js
let euro = Intl.NumberFormat('en-DE', {
    style: 'currency',
    currency: 'EUR',
    useGrouping: false,
});

console.log(`Euro: ${euro.format(price)}`);
// Euro: €143450.00
```

Another option is the `maximumSignificantDigits`. You can use this to round your price variable based on the number of significant digits you have set. For example, when you set the value to `3`, `143,450.00` will become `143,000`.

```js
let pounds = Intl.NumberFormat('en-GB', {
    style: 'currency',
    currency: 'GBP',
    maximumSignificantDigits: 3,
});

console.log(`Pounds: ${pounds.format(price)}`);
// Pounds: £143,000
```

## Voilà! 🚀

I hope this article was worth your time. You now know how to format a number as currency with JavaScript without relying on any external library.

When working with libraries like React, Vue, and others, you can make this a utility function, import it into any of your components, and use it instead of installing an entire library (unless you need more functionalities).

Have fun coding!
