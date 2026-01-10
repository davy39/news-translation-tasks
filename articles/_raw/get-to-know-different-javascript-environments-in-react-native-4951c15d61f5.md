---
title: Get to know different JavaScript environments in React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T15:57:50.000Z'
originalURL: https://freecodecamp.org/news/get-to-know-different-javascript-environments-in-react-native-4951c15d61f5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*O9VH0AoEkPaiexMT
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Khoa Pham

  React Native can be very easy to get started with, and then at some point problems
  occur and we need to dive deep into it.

  The other day we had a strange bug that was only occurring in production build,
  and in iOS only. A long backtrace ...'
---

By Khoa Pham

React Native can be very easy to [get started](https://facebook.github.io/react-native/docs/getting-started.html) with, and then at some point problems occur and we need to dive deep into it.

The other day we had a strange bug that was only occurring in production build, and in iOS only. A long backtrace in the app revealed that it was due to `Date` constructor failure.

```
const date = new Date("2019-01-18 12:00:00")
```

This returns the correct `Date` object in debug mode, but yields `Invalid Date` in release. What’s special about `Date` constructor? Here I’m using react native 0.57.5 and no `Date` libraries.

### Date constructor

The best resource for learning Javascript is via Mozilla web docs, and entering [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date):

> Creates a JavaScript `**Date**` instance that represents a single moment in time. `Date` objects use a [Unix Time Stamp](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16), an integer value that is the number of milliseconds since 1 January 1970 UTC.

Pay attention to how Date can be constructed by dateString:

> `dateString`String value representing a date. The string should be in a format recognized by the `[Date.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)` method ([IETF-compliant RFC 2822 timestamps](http://tools.ietf.org/html/rfc2822#page-14) and also a [version of ISO8601](http://www.ecma-international.org/ecma-262/5.1/#sec-15.9.1.15)).

So `Date` constructor uses static method `Date.parse` under the hood. This has very specific requirement about the format of date string that it supports

> The standard string representation of a date time string is a simplification of the ISO 8601 calendar date extended format (see [Date Time String Format](https://tc39.github.io/ecma262/#sec-date-time-string-format) section in the ECMAScript specification for more details). For example, `"2011-10-10"` (date-only form), `"2011-10-10T14:48:00"` (date-time form), or `"2011-10-10T14:48:00.000+09:00"` (date-time form with milliseconds and time zone) can be passed and will be parsed. When the time zone offset is absent, date-only forms are interpreted as a UTC time and date-time forms are interpreted as local time.

> The ECMAScript specification states: If the String does not conform to the standard format the function may fall back to any implementation–specific heuristics or implementation–specific parsing algorithm. Unrecognizable strings or dates containing illegal element values in ISO formatted strings shall cause `Date.parse()` to return `[NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)`.

The reason that we get Invalid Date in iOS must be because the code was run in two different JavaScript environments and they somehow have different implementation of the Date parsing function.

### JavaScript Environment

React Native guide has a dedicated section about [JavaScript environments](https://facebook.github.io/react-native/docs/javascript-environment).

When using React Native, you’re going to be running your JavaScript code in two environments:

* In most cases, React Native will use [JavaScriptCore](http://trac.webkit.org/wiki/JavaScriptCore), the JavaScript engine that powers Safari. Note that on iOS, JavaScriptCore does not use JIT due to the absence of writable executable memory in iOS apps.
* When using Chrome debugging, all JavaScript code runs within Chrome itself, communicating with native code via WebSockets. Chrome uses [V8](https://code.google.com/p/v8/) as its JavaScript engine.

While both environments are very similar, you may end up hitting some inconsistencies. We’re likely going to experiment with other JavaScript engines in the future, so it’s best to avoid relying on specifics of any runtime.

React Native also uses Babel and some polyfills to have some nice syntax transformers, so some of the code that we write may not be necessarily supported natively by `JavascriptCore`.

Now it is clear that while we debug our app via Chrome debugger, it works because V8 engine handles that. Now try turning off Remote JS Debugging: we can see that the above Date constructor fails, which means it is using `JavascriptCore`.

![Image](https://cdn-media-1.freecodecamp.org/images/McX7R1GC4WxTlr9sbez6pnjIDj8Fgld2VYmZ)

To confirm this issue, let’s run our app in Xcode and go to the Safari app on MacOS to enter Development menu. Select the active Simulator and choose JSContext on the current iOS app. Remember to turn off Remote JS Debugging so that the app uses JavascriptCore:

![Image](https://cdn-media-1.freecodecamp.org/images/0pzO1brfkVZl7XGUWFYYaZ1UKwradjbpBDXY)

Now open the Console in Safari dev tools, and we should have access to JavascriptCore inside our app. Try running the above `Date` constructor to confirm that it fails:

![Image](https://cdn-media-1.freecodecamp.org/images/WiSWzBJwmprcSx0WmTJWwVcpViH39wKXodYu)

### What are legit date string formats?

Since 2016, [JavascriptCore](https://webkit.org/blog/6756/es6-feature-complete/) supports most ES6 features:

> As of [r202125](https://trac.webkit.org/changeset/202125), JavaScriptCore supports all of the new features in the [ECMAScript 6 (ES6) language specification](https://tc39.github.io/ecma262/#sec-integerindexedelementget)

And it was fully confirmed a year later in [JSC ? ES6](https://webkit.org/blog/7536/jsc-loves-es6/)

> [ES2015](http://www.ecma-international.org/ecma-262/6.0/) (also known as ES6), the version of the JavaScript specification ratified in 2015, is a huge improvement to the language’s expressive power thanks to features like [classes](http://www.2ality.com/2015/02/es6-classes-final.html), [for-of](https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/), [destructuring](http://www.2ality.com/2015/01/es6-destructuring.html), [spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator), [tail calls](http://www.2ality.com/2015/06/tail-call-optimization.html), and [much more](http://kangax.github.io/compat-table/es6/)

> WebKit’s JavaScript implementation, called JSC (JavaScriptCore), [implements all of ES6](https://webkit.org/blog/6756/es6-feature-complete/)

For more details about JavaScript features supported by different JavaScript engines, visit this [ECMAScript comparison table](https://kangax.github.io/compat-table/es6/).

Now for the date string format, from [Date.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse), let’s visit ECMAScript 2015 specification to see what it says about [date string format](https://www.ecma-international.org/ecma-262/6.0/#sec-date-time-string-format):

![Image](https://cdn-media-1.freecodecamp.org/images/yzDoA6FifKgbUKjcgt3Fe-dZAlgBGNnUicJV)

ECMAScript defines a string interchange format for date-times based upon a simplification of the ISO 8601 Extended Format. The format is as follows: `**YYYY-MM-DDTHH:mm:ss.sss_Z_**`

Where the fields are as follows:

`**"T"**` appears literally in the string, to indicate the beginning of the time element.

So `JavascriptCore` requires `T` specifier and V8 can work without it. The fix for now is to always include that T specifier. This way we always follow ECMAScript standards to make sure it works across different JavaScript environments.

```
const date = new Date("2019-01-18 12:00:00".replace(' ', 'T'))
```

And now it returns correct `Date` object. There may be difference between JavascriptCore on iOS and macOS, and among different iOS versions. The lesson learned here is that we should always test our app thoroughly in production and on devices to make sure it works as expected.

