---
title: How to get started with internationalization in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T19:25:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-internationalization-in-javascript-c09a0d2cd834
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c0jA-Wr3SikV8sBhMGAihQ.png
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
seo_desc: 'By Alex Permyakov

  By adapting our apps for different languages and countries, we provide a better
  user experience. It’s simpler for users to deal with known notations for dates,
  currencies, and numbers.

  Internationalization (i18n) involves adding sup...'
---

By Alex Permyakov

By adapting our apps for different languages and countries, we provide a better user experience. It’s simpler for users to deal with known notations for dates, currencies, and numbers.

**Internationalization (i18n)** involves adding support for different languages and countries in your app. The number 18 stands for the number of letters between the first ‘i’ and the last ‘n’_._

Examples of internationalization could be Unicode support, user interface customization for different alphabets, or array sorting of non-English strings.

JavaScript implements [Internationalization API](https://www.ecma-international.org/ecma-402/1.0/) specification and defines the built-in [Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) object.

And what makes it so useful is that it has great cross-browser compatibility and [Node.js support](https://nodejs.org/api/intl.html):

![Image](https://cdn-media-1.freecodecamp.org/images/afErT9QuFCwZj5spfEzr3KwZNpNKKJGaog10)
_[https://caniuse.com/#search=intl](https://caniuse.com/#search=intl" rel="noopener" target="_blank" title=")_

### Let’s get started!

The `**Intl**` object provides access to several constructors, like:

* **Intl.DateTimeFormat** — language-sensitive date and time formatting.
* **Intl.NumberFormat —** language-sensitive number formatting.
* **Intl.PluralRules —** plural sensitive formatting and plural language rules.
* **Intl.Collator —** language-sensitive string comparison.

Creating any of these objects follows a simple pattern:

```
const formatter = new Intl.ctor(locales, options);
```

For instance, the “**de-AT”** locale: German language as it’s used in Austria:

```
const dateFormatterAT = new Intl.DateTimeFormat("de-AT");
```

Then we call the **format()** method with a provided **Date** object:

```
const date = new Date("2018-11-25");const format = dateFormatterAT.format(date); // "25.11.2018"
```

It contains only language and country codes. Soon, we will see more comprehensive examples. [Here you can find more locale examples.](http://www.lingoes.net/en/translator/langcode.htm)

We can use [navigator.language](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorLanguage/language) — the preferred language for the user, which we use as a locale:

![Image](https://cdn-media-1.freecodecamp.org/images/Yble1iDed6eDpaXr1GbDJw17eQQdBEpJLGu1)

Here instead of calling a **format** method directly, we can assign it as a function. It’s great because once we have created a specialized format function, we can use it multiple times.

Just a few lines of code and you have a localized date!

So, next, we are going to dive deeper and learn more about locales. If you are not ready for it and only want to see cool demos like this one in the picture below — go to the examples section below!

![Image](https://cdn-media-1.freecodecamp.org/images/kR8E22SSQXkyqqeWQfufLZmnFGpyNC-rvXhu)

#### Diving deeper

Well, this is enough to get an idea of how it works, but the real use cases could get way more complicated. What if we wanted to:

* display our date using the Japanese or Persian calendar
* use Thai or Arabic-Indic digits for both dates and numbers
* use simplified Chinese
* Any combination of the above ?

### What is Locale?

In order to work with this API, we have to learn more about locales. First of all, let’s give a definition.

A locale is an identifier that refers to a set of user preferences such as:

* dates and times
* numbers and currencies
* translated names for time zones, languages, and countries
* measurement units
* sort-order (collation)

A locale is not case sensitive. It’s only a **convention**.

The locale must be a string holding a [BCP 47 language tag](http://tools.ietf.org/html/rfc5646), and all part are separated by hyphens.

Let’s take a look at the next example:

![Image](https://cdn-media-1.freecodecamp.org/images/FjMty-N4Fy5h5mLMYhFSEEzXfBB-Zwybpxnw)

Again, only four lines of code ? Let’s take a look at the diagram below and examine each part of our locale:

![Image](https://cdn-media-1.freecodecamp.org/images/QRkUyedHKCodZOv823VPd-N27228EDkZZx1I)

From this picture, you can see that only the first part — language code — is required. It’s unlikely you need a locale like this. But, this is a good example of taking a look at every possible locale part and getting an idea of what a locale is.

Our locale contains all possible parts:

* **zh** (language code) — Chinese language
* **Hans** (script code) — written in simplified characters
* **CN** (country-code) — as used in China.
* **bauddha** (variant) — using a Buddhist Hybrid Sanskrit dialect
* **u-nu-hanidec** (extension) — using Han decimal numbers

Below you can find more examples for scripts, variants, and extensions.

#### Script codes

These are used with language tags to indicate which script a language is written in. For instance:

![Image](https://cdn-media-1.freecodecamp.org/images/PNwPXNYYAhR5xM2y-OLIh2QwFuAtxXxvmK4R)

#### Variant codes

Variants represent a language dialect.

![Image](https://cdn-media-1.freecodecamp.org/images/q3dQcoCGdJnMB-5jl1VhPliCNA5m5Jadrtzt)

#### Extensions

It includes different calendars and numeric systems.

**Calendars** have “u-ca-” prefix, possible values (not all included):

![Image](https://cdn-media-1.freecodecamp.org/images/OLI1LkLJbxN65CR2UOeT8BMSRc6bVVXpehvk)

**Numeric systems** have “u-nu” prefix, possible values (not all included):

![Image](https://cdn-media-1.freecodecamp.org/images/o049A-CGR9Fp4IZyTn2wI3IMy4z3ftQdbaXn)

The Iana organization is responsible for keeping [this list](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) up to date.

### Locale negotiation

The last thing we have to learn about locales is how they are resolved. We saw this example before:

```
const formatter = new Intl.ctor(locales, options);
```

The `locales` argument is specifying a single locale or an array of locales. The environment (browser or Node.js) compares it against the locales it has available and picks the best one.

There are two matching algorithms:

* **lookup** — checks from more specific to less: if **zh-Hans-SG** is not available, get **zh-Hans**, if not — **zh,** else **—** a default locale.
* **best fit** (default) — Improved algorithm. If “es-GT” — Spanish for Guatemala is requested, but not found, then instead of providing a fallback as “es”, the “es-MX” — Spanish in Mexico will be chosen.

If we provide an array of locales, then the first match wins.

So, enough theory — now is the time to practice!

### Examples

The code for the examples can be found on [GitHub](https://gist.github.com/alexpermyakov/69706e1ec5bff64efc14c15bc9e0bbcb).

#### Date/Time Formatting

![Image](https://cdn-media-1.freecodecamp.org/images/lNsn0KyU79jQIZowSVdleRqsbSWZMCB5-R9U)

Locales are not the only thing which is great about the [Intl API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl). You can modify the result in a desirable way using an `options` argument.

![Image](https://cdn-media-1.freecodecamp.org/images/-LzjP9pShGYgbi5cPuIogpGI2UCTGlbZAZzf)

This is a massive update compared to the **Date** object!

Unlike moment.js you **cannot manually swap** any part of the date like year and month. You have to use the proper locale instead. This may sound like a **limitation**, but it makes it more familiar for our users.

#### Number Formatting

Knowing how to deal with dates, you know how to deal with numbers. The only difference is the list of options:

![Image](https://cdn-media-1.freecodecamp.org/images/y-b7iSrasEiJvD2WqqDq0KDAO61HZWkDNSxN)

#### Currency Formatting

For the currencies we use `Intl.NumberFormat` constructor, but provide a different list of options:

![Image](https://cdn-media-1.freecodecamp.org/images/RyBT6EzHcO-K4UOimN3UGIEMJaWGAzQSc6xD)

Note, we don’t convert money here. All we do is format the number 172630 using **appropriate** currency rules. Here you can find the list of [currency codes](https://www.currency-iso.org/dam/downloads/lists/list_one.xml).

#### Plural Rules Formatting

This tells you which form applies based on a given number for a specific locale:

![Image](https://cdn-media-1.freecodecamp.org/images/QvzCr-RKIwnXXRLp9LbGEQM9yxoamK-tNrnc)

It can be very handy for formatting ordinal numbers:

![Image](https://cdn-media-1.freecodecamp.org/images/cjYfaoKpb7V97e5vJqDqKcdxJEO2kZoVLIdE)

#### Sorting strings

Sorting strings which contain extra letters like _ä_ in German or Swedish is not what you want to do manually, just because of the order depends on the language. Luckily for us, we have `Intl**.**Collator`. And again all we have to do is to provide a required locale:

![Image](https://cdn-media-1.freecodecamp.org/images/1V0DR0viMQe--PzGNPAoIayzO1bkpWVgZzX1)

### Conclusion

Internationalization is a great and complex topic. But if you know what a locale is and how to construct it, the rest is super easy to use.

### That’s it!

If you have any questions or feedback, let me know in the comments down below or ping me on [Twitter](https://twitter.com/AlexDevBB).

#### If this was useful, please click the clap ? button down below a few times to show your support! ⬇⬇ ??

Here are more articles I’ve written:

[**How to simplify your codebase with map(), reduce(), and filter() in JavaScript**](https://medium.freecodecamp.org/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f)  
[_When you read about Array.reduce and how cool it is, the first and sometimes the only example you find is the sum of…_medium.freecodecamp.org](https://medium.freecodecamp.org/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f)[**Production ready Node.js REST APIs Setup using TypeScript, PostgreSQL and Redis.**](https://medium.com/@alex.permyakov/production-ready-node-js-rest-apis-setup-using-typescript-postgresql-and-redis-a9525871407)  
[_A month ago I was given a task to build a simple Search API. All It had to do is to grab some data from 3rd party…_medium.com](https://medium.com/@alex.permyakov/production-ready-node-js-rest-apis-setup-using-typescript-postgresql-and-redis-a9525871407)

Thanks for reading ❤️

