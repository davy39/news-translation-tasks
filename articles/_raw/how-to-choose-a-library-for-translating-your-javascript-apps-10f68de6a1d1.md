---
title: How to choose a library for translating your JavaScript apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T08:25:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-a-library-for-translating-your-javascript-apps-10f68de6a1d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IklbYvLxPek-M3vr2wTmoA.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: translation
  slug: translation
seo_title: null
seo_desc: 'By Anastasia

  In the previous articles, we have seen how to perform localization on the back-end.
  Specifically, we’ve covered Rails and Phoenix frameworks. Today, however, we are
  going to talk about libraries for translating JavaScript apps and briefl...'
---

By Anastasia

In the previous articles, we have seen how to perform localization on the back-end. Specifically, we’ve covered [Rails](https://blog.lokalise.co/rails-i18n/) and [Phoenix](https://blog.lokalise.co/localization-of-phoenix-applications/) frameworks. Today, however, we are going to talk about libraries for translating JavaScript apps and briefly see them in action.

It appears that there are quite a lot of available solutions, so you may ask: “Which one should I use?”. The most obvious (and perhaps the sanest) answer would be: “It depends”. Ideally, you should check each library and then decide which one you prefer.

Therefore, in this article I will give you a general introduction to the following solutions:

* Globalize
* I18next
* jQuery.I18n
* Polyglot.js

Note that we will be talking about localizing vanilla JS apps, not about some specific client-side framework. Also, we won’t dive deep into each library because the article would become much, much longer. I’ll only give you a gentle introduction to each tool. Then we’ll try to compare them and come to some general conclusion.

Shall we start?

### Globalize

[Globalize](https://github.com/globalizejs/globalize) is a complex translation and localization JS library initially introduced by jQuery team. This library utilizes [Unicode common locale data repository](http://cldr.unicode.org/) (CLDR) and has lots of features including:

* Message formatting
* Date/time parsing and the ability to work with relative time
* Pluralization support
* Numbers parsing and currency formatting
* Ability to work with units (days, minutes, seconds, miles per hour etc)

Globalize works consistently in browser and NodeJS, has a modular code and allows to require as little modules as needed. While relying on CLDR data, it does not host or hardcode it directly. Developers may choose which data to load. This also means that you can update CLDR data yourself, without waiting for a new version of Globalize to be released. You may read a bit more about Globalize’s features here.

Now let’s see this library in action. There is a [Getting started guide](https://github.com/globalizejs/globalize#getting-started) that explains how to install all the required modules on your machine using a package manager. However, we’ll choose a more complex way of loading everything manually.

#### Getting CLDR Data

CLDR is really huge and so there is no reason to download all its content. Luckily, Globalize documentation [summarizes what you have to load](https://github.com/globalizejs/globalize#2-cldr-content) when using specific modules. Also, there is an [online tool](https://johnnyreilly.github.io/globalize-so-what-cha-want/#/?currency=true&date=true&message=true&number=true&plural=true&relativeTime=true&unit=true) where you just pick the modules that will be used and then see what JSON files you need to load. In this demo, I’ll only use “core”, “message”, and “plural” modules, therefore, we require the following files:

To learn more about how CLDR is organized, [refer to this doc](https://github.com/unicode-cldr/cldr-json#package-organization). It may seem complex at first but in reality, things are quite simple: you just cherry-pick the required files, download them and use in your project.

I’ve placed the files mentioned above to the `cldr/supplemental` folder of my project but you may organize them differently of course.

The next question is: how do we actually load this data? Well, [there are two alternatives](https://github.com/globalizejs/globalize/blob/master/doc/cldr.md#how-do-i-load-cldr-data-into-globalize): by embedding it inside the `Globalize.load` function or by using an [asynchronous `$.get()` method](https://api.jquery.com/jQuery.get/). The second option is much more robust, so let’s create a new JS file with the following content:

```
// i18n.js $.when( $.get("cldr/supplemental/likelySubtags.json"), $.get("cldr/supplemental/ordinals.json"), $.get("cldr/supplemental/plurals.json"), ).then(function() { // Normalize $.get results, we only need the JSON, not the request statuses. return [].slice.apply(arguments, [0]).map(function(result) { return result[0]; }); }).then(Globalize.load).then(function() { // your Globalize code here });
```

In this example, we’re loading JSON data and feed it to Globalize. We’re using promises, so the custom code should be placed into the second `then` and will be executed as soon as everything is loaded successfully. Feel free to refactor this code without using jQuery.

#### Loading Other Files

After loading CLDR JSON files, you require a [bunch of other scripts](https://github.com/globalizejs/globalize#1-dependencies):

* jQuery (note by the way that Globalize itself is not jQuery-based)
* [CLDR JS](https://github.com/rxaviers/cldrjs)
* Globalize JS core module
* Any other modules that you wish to use in your app

jQuery and Cldr.js are external dependencies and you may load them from a CDN (for example, from [cdnjs.com](https://cdnjs.com/)).

Then download Globalize from the Releases section. Open the `dist` folder. Pick all the files that you require and place them under the `globalize` directory.

After that load all the scripts in the proper order:

```
<!-- index.html --> <!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/cldrjs/0.5.1/cldr.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/cldrjs/0.5.1/cldr/event.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/cldrjs/0.5.1/cldr/supplemental.min.js"></script> <script src="globalize/globalize.js"></script> <script src="globalize/plural.js"></script> <script src="globalize/message.js"></script> <script src="i18n.js"></script> </body> </html>
```

All in all, this is it. Now you may refer to the [API section](https://github.com/globalizejs/globalize#api) of the Globalize docs and see what functions you may utilize.

#### Using It

You can provide translation messages with the help of `[loadMessages](https://github.com/globalizejs/globalize/blob/master/doc/api/message/load-messages.md)` [function](https://github.com/globalizejs/globalize/blob/master/doc/api/message/load-messages.md):

```
$.when( // ... }).then(Globalize.load).then(function() { Globalize.loadMessages({ "en": { 'welcome': 'Welcome, {name}!' } }); });
```

Then instantiate Globalize with the desired locale and perform the actual translations:

```
// loadMessages... var globalize = new Globalize("en"); console.log(globalize.messageFormatter('welcome')({name: 'Username'}));
```

`[messageFormatter](https://github.com/globalizejs/globalize/blob/master/doc/api/message/message-formatter.md)` returns a formatted translation. As you can see from this example, it supports interpolation, but there is more. Want to introduce pluralization? Simple!

Add a new message:

```
Globalize.loadMessages({ "en": { 'welcome': 'Welcome, {name}!', 'messages': [ "You have {count, plural,", " one {one message}", " other {{count} messages}", "}" ] } });
```

Note that the message may span multiple lines but in this case, it should be defined as an array. Here we are utilizing pluralization and providing two forms: singular and plural. `count` is an interpolation.

Now display this message:

```
taskFormatter = globalize.messageFormatter("messages"); console.log(taskFormatter({ count: 10 }));
```

You may utilize other modules in pretty much the same way.

To summarize, Globalize is a great powerful solution with good documentation and nice support. It may require some time to set it up but working with it is convenient and intuitive.

### I18next

I18next is a JavaScript localization framework providing all the necessary tools to translate your applications. It has loads of various features including:

* [Support for front-end frameworks](https://www.i18next.com/overview/supported-frameworks) including React, Angular, Vue etc
* Supports for various formats (including Polyglot which we’ll discuss later)
* Message formatting
* Pluralization
* Fallbacks
* Ability to load translation data from various resources
* …and many, many other [utilities and plugins](https://www.i18next.com/overview/plugins-and-utils)

#### Loading Required Files

To get started with I18next you may simply require it from CDN, for example:

```
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/i18next/14.0.1/i18next.min.js"></script> </body> </html>
```

Of course, it can be also installed with NPM or Yarn as explained [here](https://www.i18next.com/overview/getting-started).

#### Configuration

As I already mentioned above, I18next allows you to load translations from the backend. You may also provide them in the following way:

```
i18next.init({ lng: 'en', resources: { en: { translation: { "hi": "Welcome" } } } }).then(function(t) { // ready to go! });
```

Note that I am also setting English as a default locale.

There are many other configuration options that are listed on the [corresponding page](https://www.i18next.com/overview/configuration-options).

#### Using It

You may perform translations in the following way:

```
// ... init .then(function(t) { // initialized and ready to go! console.log(i18next.t('hi')); });
```

`[t](https://www.i18next.com/overview/api#t)` [is a function](https://www.i18next.com/overview/api#t) to look up translation based on the provided key. It can also work with interpolation, for instance:

```
i18next.t('hi', {name: 'Username'});
```

[Pluralization](https://www.i18next.com/translation-function/plurals) is supported too. To start using it, define singular and plural forms in the following way:

```
{ "msg": "one message", "msg_plural": "{{count}} messages" }
```

Note the `_plural` part that has to be provided for plural forms. Some languages require [multiple forms](https://www.i18next.com/translation-function/plurals#languages-with-multiple-plurals). In this case use `_0`, `_1`, and other post-fixes, for example:

```
{ "key_0": "zero", "key_1": "singular", "key_2": "two", "key_3": "few", "key_4": "many", "key_5": "other" }
```

Then just use the `t` function again:

```
i18next.t('msg', {count: 10});
```

I18next allows you to provide [context for the translation](https://www.i18next.com/translation-function/context). This is particularly important when working with gender information:

```
{ "friend": "A friend", "friend_male": "A boyfriend", "friend_female": "A girlfriend" }
```

`_male` and `_female` here are contexts that you can set in the following way:

```
i18next.t('friend'); // ==> No context here, so return "A friend" i18next.t('friend', { context: 'male' }); // -> A context is present, so return "A boyfriend"
```

Don’t hesitate to browse other examples in the I18next’s docs on how to [enable nesting in translations](https://www.i18next.com/translation-function/nesting), [work with objects](https://www.i18next.com/translation-function/objects-and-arrays), or [setup fallbacks](https://www.i18next.com/principles/fallback).

To summarize, I18next is a great framework with an array of various plugins and utilities. This framework is quite large and heavy, but you receive all the necessary localization tools that can be extended as necessary. Moreover, setting this framework up is simple and requires very little time. So, I would say this is a great candidate for complex applications!

### jQuery.I18n

[jQuery.I18n](https://github.com/wikimedia/jquery.i18n) is yet another popular solution presented to you by [Wikimedia Engineering team](https://www.mediawiki.org/wiki/Wikimedia_Language_engineering) allowing to translate your JavaScript applications. Wikimedia, in turn, is a company behind [Wikipedia project](http://en.wikipedia.org/), one of the most popular websites in the world. jQuery.I18n is used in Wikipedia internally, so you can be sure this library won’t be abandoned out of the blue. It utilizes a JSON-based localization format and supports the following [features](https://github.com/wikimedia/jquery.i18n#features):

* Ability to meta information and document your messages
* Supports pluralization with the help of CLDR
* Gender information
* Support for grammar forms
* Fallback chains
* Ability to customize message parser
* Has modular code

Let’s see jQuery.I18n in action now.

#### Loading Required Files

First of all, download the library itself and initialize its dependencies:

```
$ git clone https://github.com/wikimedia/jquery.i18n.git $ cd jquery.i18n $ git submodule update --init
```

`jquery.i18n/src` folder contains the library’s files. Pick the modules that you need (at the very least, you’ll require the core `jquery.i18n.js`) and place them to your application. The idea here is similar to the one in Globalize. The `languages` folder contains some helpers for various locales. If you are supporting one of these, don’t forget to copy the corresponding file as well.

If your application works with plural forms, then the `CLDRPluralRuleParser.js` file is necessary too (it can be found under the `jquery.i18n\libs\CLDRPluralRuleParser\src` path).

After you are ready, load the files in the proper order, for example:

```
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> <script src="lib/CLDRPluralRuleParser.js"></script> <script src="lib/jquery.i18n.js"></script> <script src="lib/jquery.i18n.messagestore.js"></script> <script src="lib/jquery.i18n.fallbacks.js"></script> <script src="lib/jquery.i18n.language.js"></script> <script src="lib/jquery.i18n.parser.js"></script> <script src="lib/jquery.i18n.emitter.js"></script> <script src="lib/jquery.i18n.emitter.bidi.js"></script> </body> </html>
```

#### Providing Translations

As mentioned above, [translations for the jQuery.I18n library](https://github.com/wikimedia/jquery.i18n#message-file-format) are stored inside JSON files. You may separate translation data for different languages, or store everything in a single file. Create a `i18n/i18n.json` file with the following contents:

```
{ "@metadata": { "authors": [ "Ilya" ], "last-updated": "2019-01-29", "message-documentation": "qqq" }, "welcome": "Hi!" }
```

[To load this file](https://github.com/wikimedia/jquery.i18n#message-loading), use the following code (note that I am also providing a default locale):

```
// main.js jQuery(document).ready(function() { $.i18n({locale: 'en'}).load({ en: 'i18n/i18n.json' }).done(function() { // success }) });
```

Include this script on your main page and you are good to go!

#### Using It

For instance, you may output a welcoming message in the following way:

```
console.log($.i18n('welcome', 'Username'));
```

[Pluralization](https://github.com/wikimedia/jquery.i18n#plurals) is performed in the following way:

```
{ "msg": "You have $1 {{PLURAL:$1|message|messages}}" }
```

So, you have one key that lists all the available forms, both plural, and singular. `$1` is a [placeholder](https://github.com/wikimedia/jquery.i18n#placeholders) for the interpolation. You may have as many placeholders as needed, and they should be named in a sequential manner: `$2`, `$3` etc.

Then just utilize this new key:

```
$.i18n('msg', 10); // $1 placeholder will have a value of 10
```

The context of the translation is defined in pretty much the same way. For example, you can work with [gender information](https://github.com/wikimedia/jquery.i18n#gender):

```
"friend": "Some text... {{GENDER:$1|A boyfriend|A girlfriend}}"
```

Provide the context:

```
$.i18n('friend', 'female');
```

One interesting feature is the support for the `[data-*](https://github.com/wikimedia/jquery.i18n#data-api)` [HTML5 attributes](https://github.com/wikimedia/jquery.i18n#data-api). You just need to add a `data-i18n` attribute to your tags, provide the key as the value, and then apply `.i18n()` function directly to those elements or their parent. For example:

```
<body> <p data-i18n="translation-key">Fallback text goes here</p> <p data-i18n="another-key">Fallback text goes here</p> </body>
```

Now inside your code simply say:

```
$('body').i18n();
```

The script is going to traverse all elements inside `body` and replace their contents with the messages under the provided translation keys. If the key cannot be found, the initial content will be displayed as a fallback.

jQuery.I18n is a powerful and quite easy-to-use library. Basically, you may call it a direct competitor to Globalize as these two solutions have similar functionality. To some people, Globalize may seem more favorable as it doesn’t rely on jQuery. On the other hand, many websites do requite jQuery, so that’s perhaps not a deal-breaker. If you’d like to mostly stay away from CLDR then jQuery.I18n is, of course, a better option. This library also allows to store metadata inside your translation files, supports `[data-*](https://github.com/wikimedia/jquery.i18n#data-api)` [attributes API](https://github.com/wikimedia/jquery.i18n#data-api), supports so-called [“magic words”](https://github.com/wikimedia/jquery.i18n#magic-word-support), and more. So, as you see, there is really a lot of features!

### Polyglot

The last solution we’ll talk about is [Polyglot.js](https://github.com/airbnb/polyglot.js) created by Airbnb. As long as Airbnb service is worldwide, it’s essential for them to have proper localization. Polyglot, in contrast to the previously discussed libraries, is a very small solution really. It has only the following features:

* Basic translation features
* Interpolation
* Pluralization

It may become an excellent candidate for smaller and less intricate apps that do not require all the complexities of, say, Globalize. Now let’s see how to get started with Polyglot!

#### Loading Files

Polyglot has no external dependencies at all, so all you need to do is hook up the main file:

```
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body> <script src="https://cdnjs.cloudflare.com/ajax/libs/polyglot.js/2.2.2/polyglot.min.js"></script> </body> </html>
```

#### Providing Translations and Using It

Now we can provide translations (aka “phrases”) and set the default locale:

```
var polyglot = new Polyglot({ locale: 'en', phrases: { "message_count": "%{smart_count} message |||| %{smart_count} messages" } });
```

In this example the default locale is English. Also, there is a `message_count` key that provides singular and plural forms separated with 4 pipelines (for other languages there may be more forms). Oddly enough, [pluralization relies on the `smart_count` interpolated value](https://github.com/airbnb/polyglot.js#pluralization), so you must provide it in the following way:

```
console.log(polyglot.t('message_count', {smart_count: 2}));
```

This is it! There is not much else to say about the translation process, as it relies only on the `t` function. You may find some more examples of using Polyglot in the [official doc](https://github.com/airbnb/polyglot.js#translation).

### Summing Everything Up

Potentially, there is a lot of different features to compare (some may be more or less relevant for your setup), but here is a brief summary of the discussed solutions:

![Image](https://cdn-media-1.freecodecamp.org/images/hj2GuNOKjpR8g-pZMcqoHPf9FegIwkGZDXEK)

A couple of things to note:

* I18next [does support various formatting](https://github.com/i18next/i18next-gitbook/blob/master/translation-function/formatting.md) but it requires external dependencies like [moment.js](https://momentjs.com/)
* jQuery.I18n requires CLDR Parser only for pluralization
* I18next provides lots of plugins to connect with the client-side framework, but other solutions can play nicely with frameworks as well (you may just need to spend more time to integrate everything)
* You may work with gender information (and, more broadly speaking, with contexts) in any library — it just may be less convenient and present more complexities

From my experience, I18next is a very powerful and feature-rich tool that you can easily get started with. At the same time, Globalize’s modular approach and relation on CLDR might be convenient, especially for larger and more complex applications. I have not used jQuery.I18n that much but as long as the Wikimedia team utilizes it, one can conclude that this is also a feasible tool with vast functionality. And, Polyglot is a nice tiny helper for simpler apps that also plays very nicely with server-side frameworks like Rails.

### Make Your Life Easier With Lokalise

Supporting multiple languages on a big website may become a serious pain. You must make sure that all the keys are translated for each and every locale. Luckily, there is a solution to this problem: the Lokalise platform that [makes working with the localization files much simpler](https://lokalise.co/features). Let me guide you through the initial setup which is nothing complex really.

* To get started, [grab your free trial](https://lokalise.co/signup)
* Create a new project, give it some name, and set English as a base language
* Click “Upload Language Files”
* Upload translation files for all your languages
* Proceed to the project, and edit your translations as needed
* You may also contact a professional translator to do the job for you
* Next simply download your files back
* Profit!

Lokalise has many more features including support for dozens of platforms and formats, and even the possibility to upload screenshots to read texts from them. So, stick with Lokalise and make your life easier!

### Conclusion

In this article, we were talking about the available tools used to translate JavaScript applications. We’ve covered Globalize, I18next and jQuery.I18n (larger and more complex solutions), as well as Polyglot which appeared to be a much simpler and smaller library. We’ve compared these libraries and came up with some conclusions about them. Hopefully, now you will be able to pick an I18n solution that entirely suits you. Don’t be afraid to research, experiment, and ultimately choose the tool that works for you! After all, it will be more complicated to switch to another localization library when your application is half-finished.

I thank you for staying with me, and until the next time!

_Originally published at [blog.lokalise.co](https://blog.lokalise.co/comparing-libraries-translating-js-apps/) on January 31, 2019._

