---
title: How to Format Compact Numbers with the JavaScript Internationalization API
subtitle: ''
author: Gerard Hynes
co_authors: []
series: null
date: '2023-01-04T15:39:17.000Z'
originalURL: https://freecodecamp.org/news/format-compact-numbers-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Format-Compact-Numbers.png
tags:
- name: api
  slug: api
- name: internationalization
  slug: internationalization
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Sometimes it can be difficult to fit large numbers into your site or app''s
  layout, especially if you have to display several of them together.

  As a result, a lot of modern sites and apps use the same format to display large
  numbers in a compact way. ...'
---

Sometimes it can be difficult to fit large numbers into your site or app's layout, especially if you have to display several of them together.

As a result, a lot of modern sites and apps use the same format to display large numbers in a compact way. For example, displaying 123,000 as 123K.

![freeCodeCamp's YouTube and Instagram profiles using compact number format.](https://www.freecodecamp.org/news/content/images/2022/12/freecodecamp_socials.png align="left")

*freeCodeCamp's YouTube and Instagram profiles using compact number format.*

You can do this by writing a custom format function, using a third-party library, or, best of all, using a built-in JavaScript API.

You can of course write your own formatter function (and there are several available on Stack Overflow) but you will end up having to check for a lot of conditions.

As an aside, since ES2021, JavaScript supports using underscores as numeric separators to make large numbers easier to read in your code.

```javascript
function formatCompactNumber(number) {
  if (number < 1000) {
    return number;
  } else if (number >= 1000 && number < 1_000_000) {
    return (number / 1000).toFixed(1) + "K";
  } else if (number >= 1_000_000 && number < 1_000_000_000) {
    return (number / 1_000_000).toFixed(1) + "M";
  } else if (number >= 1_000_000_000 && number < 1_000_000_000_000) {
    return (number / 1_000_000_000).toFixed(1) + "B";
  } else if (number >= 1_000_000_000_000 && number < 1_000_000_000_000_000) {
    return (number / 1_000_000_000_000).toFixed(1) + "T";
  }
}

formatCompactNumber(12_000);        // 12.0K
formatCompactNumber(2_000_000);     // 2.0M
formatCompactNumber(2_500_000);     // 2.5M
formatCompactNumber(6_000_000_000); // 6.0B
formatCompactNumber(6_900_000_000); // 6.9B
```

This implementation still leaves a `.0` after an even thousand, million, billion, or trillion. You could fix this using the `replace` method and a regular expression.

```js
function formatCompactNumber(number) {
  if (number < 1000) {
    return number;
  } else if (number >= 1000 && number < 1_000_000) {
    return (number / 1000).toFixed(1).replace(/\.0$/, "") + "K";
  } else if (number >= 1_000_000 && number < 1_000_000_000) {
    return (number / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  } else if (number >= 1_000_000_000 && number < 1_000_000_000_000) {
    return (number / 1_000_000_000).toFixed(1).replace(/\.0$/, "") + "B";
  } else if (number >= 1_000_000_000_000 && number < 1_000_000_000_000_000) {
    return (number / 1_000_000_000_000).toFixed(1).replace(/\.0$/, "") + "T";
  }
}
```

But what if you need to handle negative numbers? You could add another conditional.

```js
function formatCompactNumber(number) {
  if (number < 0) {
    return "-" + formatCompactNumber(-1 * number);
  }
  if (number < 1000) {
    return number;
  } else if (number >= 1000 && number < 1_000_000) {
    return (number / 1000).toFixed(1).replace(/\.0$/, "") + "K";
  } else if (number >= 1_000_000 && number < 1_000_000_000) {
    return (number / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  } else if (number >= 1_000_000_000 && number < 1_000_000_000_000) {
    return (number / 1_000_000_000).toFixed(1).replace(/\.0$/, "") + "B";
  } else if (number >= 1_000_000_000_000 && number < 1_000_000_000_000_000) {
    return (number / 1_000_000_000_000).toFixed(1).replace(/\.0$/, "") + "T";
  }
}
```

As you can probably see by now, this only scratches the surface of things you would need to consider when writing your own function for displaying compact numbers.

There are a [handful of npm packages](https://www.npmjs.com/search?q=compact%20number) for formatting numbers compactly. For example, you could install [`cldr-compact-number`](https://github.com/snewcomer/cldr-compact-number), but this would also add 3 kilobytes (or 1.2 kilobytes gzipped) to your JavaScript bundle, adding slightly to your pageload time.

Thankfully, you don't need to use any third-party libraries to format compact numbers, since there is a relatively simple solution that is natively supported in JavaScript.

## How to Use the JavaScript Internationalization API

The [JavaScript Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) helps you to support different languages and formatting conventions when working in JavaScript. This could be anything from formatting dates and times to knowing whether *a* or *ä* comes first when comparing strings.

The API has excellent browser support, with [98% support worldwide](https://caniuse.com/?search=Internationalization%20API). It works by using the `Intl` object to create a namespace for language-sensitive string comparison, number formatting, and date and time formatting.

As well as `Intl.DateTimeFormat` for formatting dates and times, and `Intl.Collator` for doing language-sensitive string comparison, there is `Intl.NumberFormat`. This lets you format numbers in a language-specific manner.

To get started, create a formatter using the `Intl.NumberFormat` constructor. Optionally, you can pass it one or more locales and an `options` object.

```js
new Intl.NumberFormat(locales, options);
```

A locale is a parameter that defines the user's language, region, or other localization preference. In this case it's an [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), such as "en-US" for US English, "zh-CH" for Mandarin, or "uk" for Ukrainian.

In the browser, you can access the user's locale using `navigator.language`. If you don't provide a locale, the API will attempt to use the user's locale from their browser.

The `options` object can contain values to control things like how to format currency, whether to use `l` or `liters`, or whether to display `+` or `-` for positive or negative values.

Once you have created a formatter, you can call its `format` method and pass it the number you want to format. It will return the number formatted according to whatever configuration you provided.

For example, you could use the Internationalization API to format financial values according to different currencies:

```js
const number = 12345678.99

const germanCurrencyFormatter = new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" });

const chineseCurrencyFormatter = new Intl.NumberFormat("zh-CH", { style: "currency", currency: "CNY" });

germanCurrencyFormatter.format(number); // 12.345.678,99 €
chineseCurrencyFormatter.format(number); // ¥12,345,678.99
```

One of the options that is available is `notation`. This controls the formatting when displaying numbers. The possible values for `notation` are:

* `"standard"` – plain number formatting according to the conventions of the locale (the default)
    
* `"scientific"` – returns the order of magnitude for a number
    
* `"engineering"` – returns the exponent of ten when the number is divisible by three
    
* `"compact"` – returns a string representing the exponent, such as K for thousands
    

So, for example, if you format the number 123456789 with the locale set to "en", you will get:

* standard: 123,456,789
    
* scientific: 1.235E8
    
* engineering: 123.457E6
    
* compact: 123M
    

If you want a formatter to display large numbers in a compact manner, set the locale to your desired locale and set `notation` to `"compact"` .

```js
const formatter = Intl.NumberFormat("en", { notation: "compact" });
```

This can be used to create a much shorter formatting function:

```js
function formatCompactNumber(number) {
  const formatter = Intl.NumberFormat("en", { notation: "compact" });
  return formatter.format(number);
}

formatCompactNumber(-57);               // -57
formatCompactNumber(999);               // 999
formatCompactNumber(8_554);             // 8.5K
formatCompactNumber(150_000);           // 150K
formatCompactNumber(3_237_512);         // 3.2M
formatCompactNumber(9_782_716_897);     // 9.8B
formatCompactNumber(7_899_693_036_970); // 7.9T
```

Now your site or app can display even the largest numbers compactly, making your layout that little bit neater and tidier.

### Thanks for reading!

I hope this quick guide helps you when you're working with large numbers in JavaScript and perhaps encourages you to explore the Internationalization API further.
